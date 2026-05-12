"""Mock-mode smoke test for the Python SDK.

Constructs a goodsender client against $BASE_URL with $GOODSENDER_API_KEY and
calls each of the 6 API methods. Prints one line per method, exits non-zero
if any method failed.
"""
from __future__ import annotations

import os
import sys
import traceback

import goodsender
from goodsender.api.domains_api import DomainsApi
from goodsender.api.emails_api import EmailsApi


BASE_URL = os.environ.get("BASE_URL", "http://localhost:4010")
API_KEY = os.environ.get("GOODSENDER_API_KEY", "test-key")

cfg = goodsender.Configuration(host=BASE_URL, access_token=API_KEY)
api = goodsender.ApiClient(cfg)
emails = EmailsApi(api)
domains = DomainsApi(api)

results: list[tuple[str, bool, str]] = []


def run(method: str, fn) -> None:
    try:
        detail = fn()
        results.append((method, True, detail))
    except Exception as exc:  # noqa: BLE001 — smoke test, surface any failure
        results.append((method, False, f"{type(exc).__name__}: {exc}"))


def _sendEmail() -> str:
    req = goodsender.SendEmailRequest(
        emails=[
            goodsender.SendEmail(
                var_from=goodsender.Address(email="sender@example.com"),
                to=[goodsender.Address(email="recipient@example.com")],
                subject="Hello",
                text_content="Body",
            )
        ]
    )
    res = emails.send_email(send_email_request=req)
    return f"sent={res.sent} declined={res.declined}"


def _sendTemplateEmail() -> str:
    req = goodsender.TemplateEmailRequest(
        var_from=goodsender.Address(email="sender@example.com"),
        to=goodsender.Address(email="recipient@example.com"),
        subject="OTP",
        template=goodsender.TemplateEmailRequestTemplate(
            template_id="otp_code", variables={"code": "123456"}
        ),
    )
    res = emails.send_template_email(template_email_request=req)
    return f"status={res.status}"


def _requestEmailConsent() -> str:
    req = goodsender.ConsentEmailRequest(
        domain="example.com",
        emails=[
            goodsender.ConsentEmailEntry("a@example.com"),
            goodsender.ConsentEmailEntry(
                goodsender.ConsentEmailRecipient(email="b@example.com", name="Bob")
            ),
        ],
    )
    res = emails.request_email_consent(consent_email_request=req)
    return f"emails={len(res.emails or [])}"


def _getEmailConsentStatus() -> str:
    res = emails.get_email_consent_status(email="user@example.com", domain="example.com")
    return f"entries={len(res)}"


def _listEmailConsents() -> str:
    res = emails.list_email_consents(domain="example.com", limit=50)
    return f"emails={len(res.emails or [])}"


def _listDomains() -> str:
    res = domains.list_domains(limit=50)
    return f"domains={len(res.domains)}"


run("sendEmail", _sendEmail)
run("sendTemplateEmail", _sendTemplateEmail)
run("requestEmailConsent", _requestEmailConsent)
run("getEmailConsentStatus", _getEmailConsentStatus)
run("listEmailConsents", _listEmailConsents)
run("listDomains", _listDomains)

for method, ok, detail in results:
    tag = "PASS" if ok else "FAIL"
    print(f"{tag}  python  {method:<22}  {detail}")

failed = sum(1 for _, ok, _ in results if not ok)
passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
