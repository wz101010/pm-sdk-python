# OAuthAccountBindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** |  | 
**platform** | **str** |  | 
**platform_name** | **str** |  | 
**avatar** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.o_auth_account_bind_request import OAuthAccountBindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAccountBindRequest from a JSON string
o_auth_account_bind_request_instance = OAuthAccountBindRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthAccountBindRequest.to_json())

# convert the object into a dict
o_auth_account_bind_request_dict = o_auth_account_bind_request_instance.to_dict()
# create an instance of OAuthAccountBindRequest from a dict
o_auth_account_bind_request_from_dict = OAuthAccountBindRequest.from_dict(o_auth_account_bind_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


