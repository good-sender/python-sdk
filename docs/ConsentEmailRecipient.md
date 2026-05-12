# ConsentEmailRecipient

Recipient envelope with optional display name. Pass this shape instead of a bare email string when you want the name to appear in the To header on the consent email and in subsequent listings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Recipient email address. Leading and trailing whitespace are stripped server-side. | 
**name** | **str** | Optional display name. Pass a non-empty string to set or replace the stored name. Passing &#x60;null&#x60;, an empty string, or omitting the field on a re-submitted recipient leaves any previously-stored name unchanged — clearing must be done via the dashboard / authenticated edit flow.  | [optional] 

## Example

```python
from goodsender.models.consent_email_recipient import ConsentEmailRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentEmailRecipient from a JSON string
consent_email_recipient_instance = ConsentEmailRecipient.from_json(json)
# print the JSON string representation of the object
print(ConsentEmailRecipient.to_json())

# convert the object into a dict
consent_email_recipient_dict = consent_email_recipient_instance.to_dict()
# create an instance of ConsentEmailRecipient from a dict
consent_email_recipient_from_dict = ConsentEmailRecipient.from_dict(consent_email_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


