# OAuthAccountPutBindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** | 头像 | [optional] 
**data** | **str** | 自定义数据 | [optional] 
**enable** | **bool** | 启用 | [optional] 

## Example

```python
from PMCore.Client.models.o_auth_account_put_bind_request import OAuthAccountPutBindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAccountPutBindRequest from a JSON string
o_auth_account_put_bind_request_instance = OAuthAccountPutBindRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthAccountPutBindRequest.to_json())

# convert the object into a dict
o_auth_account_put_bind_request_dict = o_auth_account_put_bind_request_instance.to_dict()
# create an instance of OAuthAccountPutBindRequest from a dict
o_auth_account_put_bind_request_from_dict = OAuthAccountPutBindRequest.from_dict(o_auth_account_put_bind_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


