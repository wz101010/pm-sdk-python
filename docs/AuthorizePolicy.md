# AuthorizePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**policy_name** | **str** |  | [optional] 
**authorize_type** | **str** |  | [optional] 
**policy_value** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.authorize_policy import AuthorizePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizePolicy from a JSON string
authorize_policy_instance = AuthorizePolicy.from_json(json)
# print the JSON string representation of the object
print(AuthorizePolicy.to_json())

# convert the object into a dict
authorize_policy_dict = authorize_policy_instance.to_dict()
# create an instance of AuthorizePolicy from a dict
authorize_policy_from_dict = AuthorizePolicy.from_dict(authorize_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


