# ConsentEmailEntry

Single entry in the `emails` array of a consent request. Either a bare email string (back-compat) or a `{ email, name? }` object so callers can attach a display name to a specific recipient. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Recipient email address. Leading and trailing whitespace are stripped server-side. | 
**name** | **str** | Optional display name. Pass a non-empty string to set or replace the stored name. Passing &#x60;null&#x60;, an empty string, or omitting the field on a re-submitted recipient leaves any previously-stored name unchanged — clearing must be done via the dashboard / authenticated edit flow.  | [optional] 

## Example

```python
from goodsender.models.consent_email_entry import ConsentEmailEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentEmailEntry from a JSON string
consent_email_entry_instance = ConsentEmailEntry.from_json(json)
# print the JSON string representation of the object
print(ConsentEmailEntry.to_json())

# convert the object into a dict
consent_email_entry_dict = consent_email_entry_instance.to_dict()
# create an instance of ConsentEmailEntry from a dict
consent_email_entry_from_dict = ConsentEmailEntry.from_dict(consent_email_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


