# AppSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**provider_code** | **str** |  | [optional] 
**group_code** | **str** |  | [optional] 
**code** | **str** |  | 
**value** | **str** |  | 
**tags** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**frontend_usable** | **bool** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.app_setting import AppSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppSetting from a JSON string
app_setting_instance = AppSetting.from_json(json)
# print the JSON string representation of the object
print(AppSetting.to_json())

# convert the object into a dict
app_setting_dict = app_setting_instance.to_dict()
# create an instance of AppSetting from a dict
app_setting_from_dict = AppSetting.from_dict(app_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


