# SendEmailErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 

## Example

```python
from goodsender.models.send_email_error_response import SendEmailErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailErrorResponse from a JSON string
send_email_error_response_instance = SendEmailErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SendEmailErrorResponse.to_json())

# convert the object into a dict
send_email_error_response_dict = send_email_error_response_instance.to_dict()
# create an instance of SendEmailErrorResponse from a dict
send_email_error_response_from_dict = SendEmailErrorResponse.from_dict(send_email_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


