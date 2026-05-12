# goodsender.EmailsApi

All URIs are relative to *https://api.goodsender.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_consent_status**](EmailsApi.md#get_email_consent_status) | **GET** /v1/emails/{email} | Get recipient consent status
[**list_email_consents**](EmailsApi.md#list_email_consents) | **GET** /v1/emails | List email consent statuses
[**request_email_consent**](EmailsApi.md#request_email_consent) | **POST** /v1/emails/consent | Request recipients&#39; consent to receive emails from your domain
[**send_email**](EmailsApi.md#send_email) | **POST** /v1/emails/send | Send an email or a batch of emails
[**send_template_email**](EmailsApi.md#send_template_email) | **POST** /v1/emails/template | Send a transactional email using a template


# **get_email_consent_status**
> List[EmailAccount] get_email_consent_status(email, domain=domain)

Get recipient consent status

Retrieve the current consent status for an email address. Optionally filter by sender domain.

### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.email_account import EmailAccount
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
    api_instance = goodsender.EmailsApi(api_client)
    email = 'user@example.com' # str | Email address to look up.
    domain = 'example.com' # str | Optional sender domain to filter consent records by. When omitted, returns consent across all domains. (optional)

    try:
        # Get recipient consent status
        api_response = api_instance.get_email_consent_status(email, domain=domain)
        print("The response of EmailsApi->get_email_consent_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->get_email_consent_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to look up. | 
 **domain** | **str**| Optional sender domain to filter consent records by. When omitted, returns consent across all domains. | [optional] 

### Return type

[**List[EmailAccount]**](EmailAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recipient consent status across all domains |  -  |
**400** | Invalid email address |  -  |
**404** | Email address was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_email_consents**
> EmailListResponse list_email_consents(domain, limit=limit, cursor=cursor, consent_status=consent_status, engagement_status=engagement_status)

List email consent statuses

Retrieve a paginated list of email consent statuses for a domain.

### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.email_list_response import EmailListResponse
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
    api_instance = goodsender.EmailsApi(api_client)
    domain = 'example.com' # str | Sender domain to filter consent records by.
    limit = 50 # int | Maximum number of records to return. (optional) (default to 50)
    cursor = 'cursor_example' # str | Cursor for pagination. (optional)
    consent_status = 'consent_status_example' # str | Status of the recipient's consent for receiving emails. 'pending' = awaiting consent email send, 'requested' = consent email dispatched, 'failed' = consent email delivery failed, 'granted' = recipient consented to receive emails, 'denied' = recipient declined to receive emails. (optional)
    engagement_status = 'engagement_status_example' # str | Status of the recipient's engagement with the emails. (optional)

    try:
        # List email consent statuses
        api_response = api_instance.list_email_consents(domain, limit=limit, cursor=cursor, consent_status=consent_status, engagement_status=engagement_status)
        print("The response of EmailsApi->list_email_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->list_email_consents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Sender domain to filter consent records by. | 
 **limit** | **int**| Maximum number of records to return. | [optional] [default to 50]
 **cursor** | **str**| Cursor for pagination. | [optional] 
 **consent_status** | **str**| Status of the recipient&#39;s consent for receiving emails. &#39;pending&#39; &#x3D; awaiting consent email send, &#39;requested&#39; &#x3D; consent email dispatched, &#39;failed&#39; &#x3D; consent email delivery failed, &#39;granted&#39; &#x3D; recipient consented to receive emails, &#39;denied&#39; &#x3D; recipient declined to receive emails. | [optional] 
 **engagement_status** | **str**| Status of the recipient&#39;s engagement with the emails. | [optional] 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of email consent statuses |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_email_consent**
> ConsentEmailResult request_email_consent(consent_email_request)

Request recipients' consent to receive emails from your domain

Send a consent message to each address so recipients can approve or reject future emails from your domain.
Include the email addresses in the request body to start the consent flow.


### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.consent_email_request import ConsentEmailRequest
from goodsender.models.consent_email_result import ConsentEmailResult
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
    api_instance = goodsender.EmailsApi(api_client)
    consent_email_request = goodsender.ConsentEmailRequest() # ConsentEmailRequest | 

    try:
        # Request recipients' consent to receive emails from your domain
        api_response = api_instance.request_email_consent(consent_email_request)
        print("The response of EmailsApi->request_email_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->request_email_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_email_request** | [**ConsentEmailRequest**](ConsentEmailRequest.md)|  | 

### Return type

[**ConsentEmailResult**](ConsentEmailResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recipient consent status for each address (found or created) |  -  |
**400** | Invalid request |  -  |
**429** | Too many consents are awaiting processing for this workspace. The internal release queue will drain pending entries automatically; retry later.  |  -  |
**500** | Internal server error. The upfront quota reservation (if any) is refunded and the request is safe to retry — &#x60;getOrCreateEmailsInDb&#x60; is idempotent.  |  -  |
**502** | Bad gateway - upstream email service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email**
> SendEmailResponse send_email(send_email_request)

Send an email or a batch of emails

Send one or more emails. Emails can be sent only to recipients who have opted in to receive communications from your domain.
The response indicates how many emails were sent versus not sent, based on each recipient's consent state.


### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.send_email_request import SendEmailRequest
from goodsender.models.send_email_response import SendEmailResponse
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
    api_instance = goodsender.EmailsApi(api_client)
    send_email_request = {"emails":[{"from":{"email":"sender@example.com","name":"Sender Name"},"to":[{"email":"recipient@example.com","name":"Recipient Name"}],"subject":"Test Email","text_content":"This is a test email"}]} # SendEmailRequest | List of emails to send

    try:
        # Send an email or a batch of emails
        api_response = api_instance.send_email(send_email_request)
        print("The response of EmailsApi->send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_request** | [**SendEmailRequest**](SendEmailRequest.md)| List of emails to send | 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email(s) accepted for sending |  -  |
**400** | Bad request - validation error |  -  |
**401** | Unauthorized - invalid or missing API key |  -  |
**413** | Payload too large |  -  |
**429** | Quota exceeded. |  * Retry-After - Seconds until the quota resets. <br>  |
**500** | Internal server error |  -  |
**502** | Bad gateway - upstream email service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_template_email**
> TemplateEmailResponse send_template_email(template_email_request)

Send a transactional email using a template

Send a transactional email using a predefined template for common use cases like OTP codes, order confirmations, and new device login alerts.
If the recipient has "denied" consent, the response returns `{"status": "declined"}` and the email is not sent. Unknown recipients are auto-registered with "pending" consent. The template endpoint does not change the recipient's consent.
Each email includes an approve/reject footer allowing the recipient to manage future communications.
Provide the template ID and any variables to fill in the placeholders. All variables are optional and will be replaced with an empty string if omitted.
URL-type variables must point to the same domain as the sender's email address.


### Example

* Bearer (ApiKey) Authentication (bearerAuth):

```python
import goodsender
from goodsender.models.template_email_request import TemplateEmailRequest
from goodsender.models.template_email_response import TemplateEmailResponse
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
    api_instance = goodsender.EmailsApi(api_client)
    template_email_request = {"from":{"email":"sender@example.com","name":"Sender Name"},"to":{"email":"recipient@example.com","name":"Recipient Name"},"subject":"Test Email","template":{"template_id":"otp_code","variables":{"app_name":"MyApp","otp_code":"482916"}}} # TemplateEmailRequest | Template email to send

    try:
        # Send a transactional email using a template
        api_response = api_instance.send_template_email(template_email_request)
        print("The response of EmailsApi->send_template_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->send_template_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_email_request** | [**TemplateEmailRequest**](TemplateEmailRequest.md)| Template email to send | 

### Return type

[**TemplateEmailResponse**](TemplateEmailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the templated email was sent |  -  |
**400** | Bad request - invalid variables or request body |  -  |
**401** | Unauthorized - invalid or missing API key |  -  |
**404** | Template not found |  -  |
**413** | Payload too large |  -  |
**429** | Quota exceeded. |  * Retry-After - Seconds until the quota resets. <br>  |
**500** | Internal server error |  -  |
**502** | Bad gateway - upstream email service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

