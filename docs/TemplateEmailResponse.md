# TemplateEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | \&quot;sent\&quot; if the email was sent, \&quot;declined\&quot; if the recipient has opted out | 

## Example

```python
from goodsender.models.template_email_response import TemplateEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEmailResponse from a JSON string
template_email_response_instance = TemplateEmailResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateEmailResponse.to_json())

# convert the object into a dict
template_email_response_dict = template_email_response_instance.to_dict()
# create an instance of TemplateEmailResponse from a dict
template_email_response_from_dict = TemplateEmailResponse.from_dict(template_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


