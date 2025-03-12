# ServiceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**provider_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**show** | **bool** |  | [optional] 
**show_index** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.service_group import ServiceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroup from a JSON string
service_group_instance = ServiceGroup.from_json(json)
# print the JSON string representation of the object
print(ServiceGroup.to_json())

# convert the object into a dict
service_group_dict = service_group_instance.to_dict()
# create an instance of ServiceGroup from a dict
service_group_from_dict = ServiceGroup.from_dict(service_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


