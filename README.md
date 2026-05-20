# GoodSender SDK for Python

Official client library for the GoodSender email API. Package: `goodsender`

## Installation

```bash
pip install goodsender
```

## Quick start

```python
import goodsender
from goodsender.api.emails_api import EmailsApi
from goodsender.api.domains_api import DomainsApi

cfg = goodsender.Configuration(
    host="https://api.goodsender.com",
    access_token="YOUR_API_KEY",
)
api = goodsender.ApiClient(cfg)
emails = EmailsApi(api)
domains = DomainsApi(api)

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
print(f"sent={res.sent} declined={res.declined}")
```

## Examples

### Send via a template

```python
req = goodsender.TemplateEmailRequest(
    var_from=goodsender.Address(email="sender@example.com"),
    to=goodsender.Address(email="recipient@example.com"),
    subject="Your OTP",
    template=goodsender.TemplateEmailRequestTemplate(
        template_id="otp_code", variables={"code": "123456"}
    ),
)
res = emails.send_template_email(template_email_request=req)
print(f"status={res.status}")
```

### List domains

```python
res = domains.list_domains(limit=50)
for d in res.domains:
    print(d)
```

### Check consent status

```python
# Get all consent records for an address
res = emails.get_email_consent_status(email="user@example.com", domain="example.com")
print(f"entries={len(res)}")

# List all consents for a domain
res = emails.list_email_consents(domain="example.com", limit=50)
print(f"emails={len(res.emails or [])}")
```

## Documentation

- API reference: <https://api.goodsender.com/docs>
- OpenAPI spec: `openapi/goodsender.yaml` in this repo
- Conformance tests: `tests/`

## Development

- Regenerate from spec: `scripts/regen.sh` (preserves `tests/`, `.github/`, and hand-curated files per `.regen-ignore`)
- Run conformance tests against local mock: `tests/run.sh mock`
- Run conformance against real dev API: `tests/run.sh dev` (requires `tests/.env.dev`)

## License

MIT — see [LICENSE](LICENSE).
