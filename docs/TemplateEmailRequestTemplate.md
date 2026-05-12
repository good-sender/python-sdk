# TemplateEmailRequestTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | The ID of the template to use | 
**variables** | **Dict[str, str]** | Key-value pairs to populate template variables | [optional] 

## Example

```python
from goodsender.models.template_email_request_template import TemplateEmailRequestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEmailRequestTemplate from a JSON string
template_email_request_template_instance = TemplateEmailRequestTemplate.from_json(json)
# print the JSON string representation of the object
print(TemplateEmailRequestTemplate.to_json())

# convert the object into a dict
template_email_request_template_dict = template_email_request_template_instance.to_dict()
# create an instance of TemplateEmailRequestTemplate from a dict
template_email_request_template_from_dict = TemplateEmailRequestTemplate.from_dict(template_email_request_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


