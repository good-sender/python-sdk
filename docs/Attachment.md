# Attachment

Either inline_id or file_name is required. Content must be base64 encoded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name for the attachment | [optional] [default to '']
**content** | **bytes** | Base64 encoded content | [optional] 
**content_type** | **str** | MIME content type (required) | [default to '']
**inline_id** | **str** | Inline attachment ID | [optional] [default to '']

## Example

```python
from goodsender.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


