# EmailListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**List[EmailAccount]**](EmailAccount.md) |  | 
**next_cursor** | **str** | Cursor to retrieve the next page of results. Omitted if there are no more results. | [optional] 

## Example

```python
from goodsender.models.email_list_response import EmailListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailListResponse from a JSON string
email_list_response_instance = EmailListResponse.from_json(json)
# print the JSON string representation of the object
print(EmailListResponse.to_json())

# convert the object into a dict
email_list_response_dict = email_list_response_instance.to_dict()
# create an instance of EmailListResponse from a dict
email_list_response_from_dict = EmailListResponse.from_dict(email_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


