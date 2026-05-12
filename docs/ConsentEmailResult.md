# ConsentEmailResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**List[EmailAccount]**](EmailAccount.md) |  | 

## Example

```python
from goodsender.models.consent_email_result import ConsentEmailResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentEmailResult from a JSON string
consent_email_result_instance = ConsentEmailResult.from_json(json)
# print the JSON string representation of the object
print(ConsentEmailResult.to_json())

# convert the object into a dict
consent_email_result_dict = consent_email_result_instance.to_dict()
# create an instance of ConsentEmailResult from a dict
consent_email_result_from_dict = ConsentEmailResult.from_dict(consent_email_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


