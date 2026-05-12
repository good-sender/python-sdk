# TrackingSettings

Controls email tracking and unsubscribe settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opens** | **bool** | Whether to track email opens | [optional] 
**clicks** | **bool** | Whether to track link clicks | [optional] 
**unsubscribes** | **bool** | Whether to track unsubscribes | [optional] 
**unsubscribe_group_id** | **int** | Optional unsubscribe group ID. If not specified, uses global unsubscribe list. This setting is ignored if unsubscribes is false. | [optional] 

## Example

```python
from goodsender.models.tracking_settings import TrackingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingSettings from a JSON string
tracking_settings_instance = TrackingSettings.from_json(json)
# print the JSON string representation of the object
print(TrackingSettings.to_json())

# convert the object into a dict
tracking_settings_dict = tracking_settings_instance.to_dict()
# create an instance of TrackingSettings from a dict
tracking_settings_from_dict = TrackingSettings.from_dict(tracking_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


