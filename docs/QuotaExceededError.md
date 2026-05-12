# QuotaExceededError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Machine-readable error code. | 
**kind** | **str** | Whether the daily or monthly quota was exhausted. | 
**message** | **str** | Human-readable error message. | 
**limit** | **int** | Quota limit that was reached. | 
**used** | **int** | Number of emails already used against the quota. | 
**reset_at** | **datetime** | Timestamp at which the quota window resets. | 

## Example

```python
from goodsender.models.quota_exceeded_error import QuotaExceededError

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaExceededError from a JSON string
quota_exceeded_error_instance = QuotaExceededError.from_json(json)
# print the JSON string representation of the object
print(QuotaExceededError.to_json())

# convert the object into a dict
quota_exceeded_error_dict = quota_exceeded_error_instance.to_dict()
# create an instance of QuotaExceededError from a dict
quota_exceeded_error_from_dict = QuotaExceededError.from_dict(quota_exceeded_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


