# TemplateEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**Address**](Address.md) | Sender address (required) | 
**to** | [**Address**](Address.md) | Recipient address (required) | 
**subject** | **str** | The subject of the email (required) | 
**template** | [**TemplateEmailRequestTemplate**](TemplateEmailRequestTemplate.md) |  | 

## Example

```python
from goodsender.models.template_email_request import TemplateEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEmailRequest from a JSON string
template_email_request_instance = TemplateEmailRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateEmailRequest.to_json())

# convert the object into a dict
template_email_request_dict = template_email_request_instance.to_dict()
# create an instance of TemplateEmailRequest from a dict
template_email_request_from_dict = TemplateEmailRequest.from_dict(template_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


