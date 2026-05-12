# ConsentEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain for the email addresses. | 
**redirect_url** | **str** | URL to which the user will be redirected after providing consent. {email} in the URL will be replaced with the recipient&#39;s email address. | [optional] 
**emails** | [**List[ConsentEmailEntry]**](ConsentEmailEntry.md) | Recipients to request consent from. Each entry may be either a plain email string or a &#x60;{ email, name? }&#x60; object so callers can attach a display name to a specific recipient. Mixing the two forms in one request is allowed.  | 

## Example

```python
from goodsender.models.consent_email_request import ConsentEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentEmailRequest from a JSON string
consent_email_request_instance = ConsentEmailRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentEmailRequest.to_json())

# convert the object into a dict
consent_email_request_dict = consent_email_request_instance.to_dict()
# create an instance of ConsentEmailRequest from a dict
consent_email_request_from_dict = ConsentEmailRequest.from_dict(consent_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


