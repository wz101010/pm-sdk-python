# App


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**website** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**app_key** | **str** |  | [optional] 
**app_secret** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**ssh_publickey** | **str** |  | [optional] 
**share** | **bool** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**show** | **bool** |  | [optional] 
**show_index** | **int** |  | [optional] 

## Example

```python
from PMCore.Client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


