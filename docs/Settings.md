# Settings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**biz_code** | **str** |  | [optional] 
**biz_identity** | **str** |  | [optional] 
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
from PMCore.Client.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print(Settings.to_json())

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_from_dict = Settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


