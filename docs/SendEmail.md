# SendEmail

Must provide valid sender and subject. At least one recipient (from 'to', 'cc', or 'bcc') is required. Either 'text_content', 'html_content', 'markdown_content', or 'template_id' is required. When 'markdown_content' is provided, 'text_content' and 'html_content' are ignored. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**Address**](Address.md) | Sender address (required) | 
**to** | [**List[Address]**](Address.md) | To recipients. At least one recipient (to, cc, or bcc) is required. Maximum 1000 recipients per email. | 
**subject** | **str** | The subject of the email (required) | [default to '']
**text_content** | **str** | Plain text content | [optional] 
**html_content** | **str** | HTML content | [optional] 
**markdown_content** | **str** | Markdown content. When provided, text_content and html_content are ignored. The raw markdown is used as text_content and rendered to HTML for html_content.  | [optional] 
**template_id** | **str** | Template ID for templated emails | [optional] 
**template_data** | **Dict[str, object]** | Data to populate template variables | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Email attachments | [optional] 
**headers** | **Dict[str, str]** | Custom email headers | [optional] 
**reply_to** | [**Address**](Address.md) | Reply-to address | [optional] 
**send_time** | **int** | Unix timestamp for when to send the email. Must not be more than 72 hours in the future. If 0, sends immediately. | [optional] 
**webhook_data** | **Dict[str, str]** | Custom data to include in webhook events. Maximum 10 keys, key length 50 chars, value length 100 chars. | [optional] 
**tag** | **str** | Custom tag for tracking. Maximum 100 characters. | [optional] 
**tracking** | [**TrackingSettings**](TrackingSettings.md) | Email tracking settings | [optional] 

## Example

```python
from goodsender.models.send_email import SendEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmail from a JSON string
send_email_instance = SendEmail.from_json(json)
# print the JSON string representation of the object
print(SendEmail.to_json())

# convert the object into a dict
send_email_dict = send_email_instance.to_dict()
# create an instance of SendEmail from a dict
send_email_from_dict = SendEmail.from_dict(send_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


