# UserSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**provider_code** | **str** |  | [optional] 
**group_code** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**frontend_usable** | **bool** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.user_setting import UserSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UserSetting from a JSON string
user_setting_instance = UserSetting.from_json(json)
# print the JSON string representation of the object
print(UserSetting.to_json())

# convert the object into a dict
user_setting_dict = user_setting_instance.to_dict()
# create an instance of UserSetting from a dict
user_setting_from_dict = UserSetting.from_dict(user_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


