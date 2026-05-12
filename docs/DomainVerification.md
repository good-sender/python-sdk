# DomainVerification

Per-record verification state for the domain. `verified` is the overall flag; the individual `*_verified` fields indicate which DNS records still need attention when `verified` is `false`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** | Overall verification status. True only when every required DNS record is in place. | 
**tracking_verified** | **bool** | Whether the tracking subdomain CNAME is in place. | 
**return_path_verified** | **bool** | Whether the return-path subdomain CNAME is in place. | 
**dkim1_verified** | **bool** | Whether the first DKIM record is in place. | 
**dkim2_verified** | **bool** | Whether the second DKIM record is in place. | 

## Example

```python
from goodsender.models.domain_verification import DomainVerification

# TODO update the JSON string below
json = "{}"
# create an instance of DomainVerification from a JSON string
domain_verification_instance = DomainVerification.from_json(json)
# print the JSON string representation of the object
print(DomainVerification.to_json())

# convert the object into a dict
domain_verification_dict = domain_verification_instance.to_dict()
# create an instance of DomainVerification from a dict
domain_verification_from_dict = DomainVerification.from_dict(domain_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


