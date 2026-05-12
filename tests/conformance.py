"""State-aware conformance test for the Python SDK against the real dev API.

Mirrors tests/runners/node/conformance.ts (same scenario IDs and assertions).
Fixtures loaded from tests/.env.dev via run.sh; see tests/.env.example.
Destructive scenarios (D*, E*) run only when ALLOW_DESTRUCTIVE=1.
"""
from __future__ import annotations

import os
import random
import string
import sys
import time
from typing import Callable

import goodsender
from goodsender.api.domains_api import DomainsApi
from goodsender.api.emails_api import EmailsApi
from goodsender.exceptions import ApiException


def _require(key: str) -> str:
    v = os.environ.get(key)
    if not v:
        print(f"FATAL: {key} is not set in .env.dev")
        sys.exit(2)
    return v


BASE_URL = _require("BASE_URL")
API_KEY = _require("GOODSENDER_API_KEY")
ALLOW_DESTRUCTIVE = os.environ.get("ALLOW_DESTRUCTIVE") == "1"

VERIFIED_DOMAIN = _require("VERIFIED_SENDER_DOMAIN")
VERIFIED_EMAIL = _require("VERIFIED_SENDER_EMAIL")
VERIFIED_NAME = os.environ.get("VERIFIED_SENDER_NAME", "GoodSender SDK Tests")
UNVERIFIED_DOMAIN = _require("UNVERIFIED_SENDER_DOMAIN")
UNVERIFIED_EMAIL = _require("UNVERIFIED_SENDER_EMAIL")
GRANTED_1 = _require("RECIPIENT_GRANTED_1")
GRANTED_2 = _require("RECIPIENT_GRANTED_2")
DENIED_1 = _require("RECIPIENT_DENIED_1")
DENIED_2 = _require("RECIPIENT_DENIED_2")
TEMPLATE_ID = _require("TEMPLATE_ID")

RUN_TAG = f"sdk-{int(time.time()):x}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}"
FRESH_1 = f"{RUN_TAG}-1@{VERIFIED_DOMAIN}"
FRESH_2 = f"{RUN_TAG}-2@{VERIFIED_DOMAIN}"

cfg = goodsender.Configuration(host=BASE_URL, access_token=API_KEY)
api_client = goodsender.ApiClient(cfg)
emails = EmailsApi(api_client)
domains = DomainsApi(api_client)

results: list[tuple[str, str, str, str]] = []  # (id, name, status, detail)


def record(scenario_id: str, name: str, status: str, detail: str) -> None:
    results.append((scenario_id, name, status, detail))


def scenario(scenario_id: str, name: str, fn: Callable[[], tuple[bool, str]]) -> None:
    try:
        ok, detail = fn()
        record(scenario_id, name, "PASS" if ok else "FAIL", detail)
    except Exception as exc:  # noqa: BLE001
        record(scenario_id, name, "FAIL", f"unexpected: {type(exc).__name__}: {exc}")


def skip(scenario_id: str, name: str, reason: str) -> None:
    record(scenario_id, name, "SKIP", reason)


def http_status(exc: Exception) -> int | None:
    if isinstance(exc, ApiException):
        return exc.status
    return None


def http_body(exc: Exception) -> str:
    if isinstance(exc, ApiException):
        body = exc.body or ""
        return str(body)[:160]
    return ""


# ─── Read-only (R1–R6) ─────────────────────────────────────────────

def r1() -> tuple[bool, str]:
    res = domains.list_domains(limit=100)
    by_name = {d.domain: d for d in res.domains}
    v = by_name.get(VERIFIED_DOMAIN)
    u = by_name.get(UNVERIFIED_DOMAIN)
    if not v:
        return False, f"{VERIFIED_DOMAIN} not in listDomains response"
    if not u:
        return False, f"{UNVERIFIED_DOMAIN} not in listDomains response"
    if not v.verification.verified:
        return False, f"{VERIFIED_DOMAIN} has verification.verified=false; should be true"
    if u.verification.verified:
        return False, f"{UNVERIFIED_DOMAIN} has verification.verified=true; should be false"
    return True, f"domains={len(res.domains)}, verified=true, unverified=false"


scenario("R1", "listDomains returns both fixtures with correct verification flags", r1)


def r2() -> tuple[bool, str]:
    res = emails.get_email_consent_status(GRANTED_1, domain=VERIFIED_DOMAIN)
    entry = next((e for e in res if e.domain == VERIFIED_DOMAIN), None)
    if not entry:
        return False, f"no entry for domain={VERIFIED_DOMAIN}"
    if entry.consent_status != "granted":
        return False, f"consentStatus={entry.consent_status}, expected granted"
    return True, f"consentStatus={entry.consent_status}"


scenario("R2", "getEmailConsentStatus returns granted for approved recipient", r2)


def r3() -> tuple[bool, str]:
    res = emails.get_email_consent_status(DENIED_1, domain=VERIFIED_DOMAIN)
    entry = next((e for e in res if e.domain == VERIFIED_DOMAIN), None)
    if not entry:
        return False, f"no entry for domain={VERIFIED_DOMAIN}"
    if entry.consent_status != "denied":
        return False, f"consentStatus={entry.consent_status}, expected denied"
    return True, f"consentStatus={entry.consent_status}"


scenario("R3", "getEmailConsentStatus returns denied for rejected recipient", r3)


def r4() -> tuple[bool, str]:
    probe = f"{RUN_TAG}-r4-probe@{VERIFIED_DOMAIN}"
    try:
        res = emails.get_email_consent_status(probe, domain=VERIFIED_DOMAIN)
        return False, f"expected 404, got 200 with {len(res)} entries"
    except ApiException as exc:
        if exc.status == 404:
            return True, f"404 (probe={probe})"
        return False, f"expected 404, got {exc.status} {http_body(exc)}"


scenario("R4", "getEmailConsentStatus returns 404 for unknown recipient", r4)


def r5() -> tuple[bool, str]:
    collected: list[str] = []
    cursor: str | None = None
    for _ in range(20):
        res = emails.list_email_consents(VERIFIED_DOMAIN, limit=100, cursor=cursor)
        collected.extend(e.email for e in (res.emails or []))
        cursor = res.next_cursor
        if not cursor:
            break
    expected = [GRANTED_1, GRANTED_2, DENIED_1, DENIED_2]
    missing = [e for e in expected if e not in collected]
    if missing:
        return False, f"missing from listEmailConsents: {', '.join(missing)}"
    return True, f"{len(collected)} entries scanned; all 4 fixtures present"


scenario("R5", "listEmailConsents for verified domain includes all 4 fixtures", r5)


def r6() -> tuple[bool, str]:
    collected: set[str] = set()
    statuses: set[str] = set()
    cursor: str | None = None
    pages = 0
    for _ in range(20):
        res = emails.list_email_consents(VERIFIED_DOMAIN, consent_status="granted", limit=100, cursor=cursor)
        pages += 1
        for e in res.emails or []:
            collected.add(e.email)
            statuses.add(e.consent_status)
        cursor = res.next_cursor
        if not cursor:
            break
    if statuses - {"granted"}:
        return False, f"filter leaked non-granted statuses: {','.join(sorted(statuses))}"
    missing = [e for e in (GRANTED_1, GRANTED_2) if e not in collected]
    if missing:
        sample = ", ".join(sorted(collected)[:5]) or "(none)"
        return False, f"filter returned {len(collected)} entries across {pages} page(s); missing={','.join(missing)}; sample=[{sample}]"
    if DENIED_1 in collected or DENIED_2 in collected:
        return False, "denied fixtures leaked into granted filter"
    return True, f"{len(collected)} granted entries; denied fixtures absent"


scenario("R6", "listEmailConsents with consentStatus=granted filter excludes denied", r6)

# ─── Destructive (D1–D6, E1–E5) ────────────────────────────────────

if ALLOW_DESTRUCTIVE:

    def d1() -> tuple[bool, str]:
        req = goodsender.SendEmailRequest(emails=[goodsender.SendEmail(
            var_from=goodsender.Address(email=VERIFIED_EMAIL, name=VERIFIED_NAME),
            to=[goodsender.Address(email=GRANTED_1), goodsender.Address(email=GRANTED_2)],
            subject=f"SDK conformance D1 {RUN_TAG}",
            text_content="Conformance test D1 — to granted recipients.",
        )])
        res = emails.send_email(send_email_request=req)
        if res.sent != 2 or res.declined != 0:
            return False, f"sent={res.sent} declined={res.declined}, expected 2/0"
        return True, f"sent={res.sent} declined={res.declined}"

    scenario("D1", "sendEmail to 2 granted recipients delivers both", d1)

    def d2() -> tuple[bool, str]:
        req = goodsender.SendEmailRequest(emails=[goodsender.SendEmail(
            var_from=goodsender.Address(email=VERIFIED_EMAIL, name=VERIFIED_NAME),
            to=[goodsender.Address(email=DENIED_1), goodsender.Address(email=DENIED_2)],
            subject=f"SDK conformance D2 {RUN_TAG}",
            text_content="D2",
        )])
        res = emails.send_email(send_email_request=req)
        if res.sent != 0 or res.declined != 2:
            return False, f"sent={res.sent} declined={res.declined}, expected 0/2"
        return True, f"sent={res.sent} declined={res.declined}"

    scenario("D2", "sendEmail to 2 denied recipients declines both", d2)

    def d3() -> tuple[bool, str]:
        req = goodsender.SendEmailRequest(emails=[goodsender.SendEmail(
            var_from=goodsender.Address(email=VERIFIED_EMAIL, name=VERIFIED_NAME),
            to=[goodsender.Address(email=GRANTED_1), goodsender.Address(email=DENIED_1)],
            subject=f"SDK conformance D3 {RUN_TAG}",
            text_content="D3",
        )])
        res = emails.send_email(send_email_request=req)
        if res.sent != 1 or res.declined != 1:
            return False, f"sent={res.sent} declined={res.declined}, expected 1/1"
        return True, f"sent={res.sent} declined={res.declined}"

    scenario("D3", "sendEmail granted+denied mix splits correctly", d3)

    def d4() -> tuple[bool, str]:
        req = goodsender.TemplateEmailRequest(
            var_from=goodsender.Address(email=VERIFIED_EMAIL, name=VERIFIED_NAME),
            to=goodsender.Address(email=GRANTED_1),
            subject=f"SDK conformance D4 {RUN_TAG}",
            template=goodsender.TemplateEmailRequestTemplate(template_id=TEMPLATE_ID, variables={}),
        )
        res = emails.send_template_email(template_email_request=req)
        if res.status != "sent":
            return False, f"status={res.status}, expected sent"
        return True, f"status={res.status}"

    scenario("D4", "sendTemplateEmail to granted recipient returns status=sent", d4)

    def d5() -> tuple[bool, str]:
        req = goodsender.TemplateEmailRequest(
            var_from=goodsender.Address(email=VERIFIED_EMAIL, name=VERIFIED_NAME),
            to=goodsender.Address(email=DENIED_1),
            subject=f"SDK conformance D5 {RUN_TAG}",
            template=goodsender.TemplateEmailRequestTemplate(template_id=TEMPLATE_ID, variables={}),
        )
        res = emails.send_template_email(template_email_request=req)
        if res.status != "declined":
            return False, f"status={res.status}, expected declined"
        return True, f"status={res.status}"

    scenario("D5", "sendTemplateEmail to denied recipient returns status=declined", d5)

    def d6() -> tuple[bool, str]:
        req = goodsender.ConsentEmailRequest(domain=VERIFIED_DOMAIN, emails=[
            goodsender.ConsentEmailEntry(goodsender.ConsentEmailRecipient(email=FRESH_1, name="Fresh 1")),
            goodsender.ConsentEmailEntry(goodsender.ConsentEmailRecipient(email=FRESH_2, name="Fresh 2")),
        ])
        res = emails.request_email_consent(consent_email_request=req)
        entries = res.emails or []
        if len(entries) != 2:
            return False, f"expected 2 entries in ConsentEmailResult.emails, got {len(entries)}"
        statuses = sorted(e.consent_status for e in entries)
        return True, f"2 fresh addresses; statuses=[{','.join(statuses)}] {FRESH_1} {FRESH_2}"

    scenario("D6", "requestEmailConsent registers 2 fresh addresses", d6)

    def e1() -> tuple[bool, str]:
        try:
            req = goodsender.SendEmailRequest(emails=[goodsender.SendEmail(
                var_from=goodsender.Address(email=UNVERIFIED_EMAIL),
                to=[goodsender.Address(email=GRANTED_1)],
                subject=f"SDK conformance E1 {RUN_TAG}",
                text_content="should be rejected",
            )])
            res = emails.send_email(send_email_request=req)
            return False, f"expected 4xx, got 200 sent={res.sent}"
        except ApiException as exc:
            if exc.status and 400 <= exc.status < 500:
                return True, f"{exc.status} {http_body(exc)}"
            return False, f"expected 4xx, got {exc.status} {http_body(exc)}"

    scenario("E1", "sendEmail from unverified domain is rejected", e1)

    def e2() -> tuple[bool, str]:
        try:
            req = goodsender.TemplateEmailRequest(
                var_from=goodsender.Address(email=UNVERIFIED_EMAIL),
                to=goodsender.Address(email=GRANTED_1),
                subject=f"SDK conformance E2 {RUN_TAG}",
                template=goodsender.TemplateEmailRequestTemplate(template_id=TEMPLATE_ID, variables={}),
            )
            res = emails.send_template_email(template_email_request=req)
            return False, f"expected 4xx, got 200 status={res.status}"
        except ApiException as exc:
            if exc.status and 400 <= exc.status < 500:
                return True, f"{exc.status} {http_body(exc)}"
            return False, f"expected 4xx, got {exc.status} {http_body(exc)}"

    scenario("E2", "sendTemplateEmail from unverified domain is rejected", e2)

    def e3() -> tuple[bool, str]:
        bad_template = f"{RUN_TAG}-does-not-exist"
        try:
            req = goodsender.TemplateEmailRequest(
                var_from=goodsender.Address(email=VERIFIED_EMAIL),
                to=goodsender.Address(email=GRANTED_1),
                subject=f"SDK conformance E3 {RUN_TAG}",
                template=goodsender.TemplateEmailRequestTemplate(template_id=bad_template, variables={}),
            )
            res = emails.send_template_email(template_email_request=req)
            return False, f"expected 404, got 200 status={res.status}"
        except ApiException as exc:
            if exc.status == 404:
                return True, f"404 {http_body(exc)}"
            return False, f"expected 404, got {exc.status} {http_body(exc)}"

    scenario("E3", "sendTemplateEmail with bogus template_id returns 404", e3)

    def e4() -> tuple[bool, str]:
        fresh = f"{RUN_TAG}-e4-target@example.com"
        try:
            req = goodsender.ConsentEmailRequest(domain=UNVERIFIED_DOMAIN, emails=[
                goodsender.ConsentEmailEntry(fresh),
            ])
            res = emails.request_email_consent(consent_email_request=req)
            return False, f"expected 4xx, got 200 emails={len(res.emails or [])}"
        except ApiException as exc:
            if exc.status and 400 <= exc.status < 500:
                return True, f"{exc.status} {http_body(exc)}"
            return False, f"expected 4xx, got {exc.status} {http_body(exc)}"

    scenario("E4", "requestEmailConsent for unverified domain is rejected", e4)

    def e5() -> tuple[bool, str]:
        bogus = f"not-a-real-domain-{RUN_TAG}.invalid"
        try:
            res = emails.list_email_consents(bogus, limit=1)
            return True, f"200 emails={len(res.emails or [])} (no error path for unknown domain)"
        except ApiException as exc:
            if exc.status and 400 <= exc.status < 500:
                return True, f"{exc.status} {http_body(exc)}"
            return False, f"unexpected: {exc.status} {http_body(exc)}"

    scenario("E5", "listEmailConsents for non-existent domain", e5)

else:
    for sid, name in [
        ("D1", "sendEmail to 2 granted recipients"),
        ("D2", "sendEmail to 2 denied recipients"),
        ("D3", "sendEmail granted+denied mix"),
        ("D4", "sendTemplateEmail to granted"),
        ("D5", "sendTemplateEmail to denied"),
        ("D6", "requestEmailConsent for 2 fresh addresses"),
        ("E1", "sendEmail from unverified domain rejected"),
        ("E2", "sendTemplateEmail from unverified domain rejected"),
        ("E3", "sendTemplateEmail with bogus template_id"),
        ("E4", "requestEmailConsent for unverified domain rejected"),
        ("E5", "listEmailConsents for non-existent domain"),
    ]:
        skip(sid, name, "destructive — set ALLOW_DESTRUCTIVE=1")

# ─── Report ────────────────────────────────────────────────────────

for sid, name, status, detail in results:
    print(f"{status:<4}  python  {sid}  {name[:58]:<58}  {detail}")

passed = sum(1 for _, _, s, _ in results if s == "PASS")
failed = sum(1 for _, _, s, _ in results if s == "FAIL")
skipped = sum(1 for _, _, s, _ in results if s == "SKIP")
print(f"\n{passed} passed, {failed} failed, {skipped} skipped")
if ALLOW_DESTRUCTIVE:
    print(f"\nDestructive run created consent records for cleanup:\n  {FRESH_1}\n  {FRESH_2}")
sys.exit(1 if failed else 0)
