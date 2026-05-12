# EmailAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Recipient email address. | 
**name** | **str** | Optional display name for the recipient. Used in the To header on the consent email when present, and surfaced through the Dashboard. May be null when no name has been provided. | [optional] 
**domain** | **str** | Domain part of the email address. | 
**consent_status** | **str** | Status of the recipient&#39;s consent for receiving emails. &#39;pending&#39; &#x3D; awaiting consent email send, &#39;requested&#39; &#x3D; consent email dispatched, &#39;failed&#39; &#x3D; consent email delivery failed, &#39;granted&#39; &#x3D; recipient consented to receive emails, &#39;denied&#39; &#x3D; recipient declined to receive emails. | 
**engagement_status** | **str** | Status of the recipient&#39;s engagement with the emails. | [optional] 

## Example

```python
from goodsender.models.email_account import EmailAccount

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAccount from a JSON string
email_account_instance = EmailAccount.from_json(json)
# print the JSON string representation of the object
print(EmailAccount.to_json())

# convert the object into a dict
email_account_dict = email_account_instance.to_dict()
# create an instance of EmailAccount from a dict
email_account_from_dict = EmailAccount.from_dict(email_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


