# goodsender.DomainsApi

All URIs are relative to *https://api.goodsender.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_domains**](DomainsApi.md#list_domains) | **GET** /v1/domains | List domains


# **list_domains**
> DomainListResponse list_domains(limit=limit, cursor=cursor)

List domains

Retrieve a paginated list of sender domains for the workspace the
API key belongs to. Each entry includes the domain's verification
state so callers can detect when DNS records still need attention.


### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.domain_list_response import DomainListResponse
from goodsender.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.goodsender.com
# See configuration.py for a list of all supported configuration parameters.
configuration = goodsender.Configuration(
    host = "https://api.goodsender.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiKey): bearerAuth
configuration = goodsender.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with goodsender.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = goodsender.DomainsApi(api_client)
    limit = 50 # int | Maximum number of records to return. (optional) (default to 50)
    cursor = 'cursor_example' # str | Cursor for pagination, returned as `nextCursor` from a previous response. (optional)

    try:
        # List domains
        api_response = api_instance.list_domains(limit=limit, cursor=cursor)
        print("The response of DomainsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of records to return. | [optional] [default to 50]
 **cursor** | **str**| Cursor for pagination, returned as &#x60;nextCursor&#x60; from a previous response. | [optional] 

### Return type

[**DomainListResponse**](DomainListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of domains for the workspace. |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Unauthorized - invalid or missing API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

