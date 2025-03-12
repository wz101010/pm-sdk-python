# ServiceProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**biz_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**show** | **bool** |  | [optional] 
**show_index** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.service_provider import ServiceProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProvider from a JSON string
service_provider_instance = ServiceProvider.from_json(json)
# print the JSON string representation of the object
print(ServiceProvider.to_json())

# convert the object into a dict
service_provider_dict = service_provider_instance.to_dict()
# create an instance of ServiceProvider from a dict
service_provider_from_dict = ServiceProvider.from_dict(service_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


