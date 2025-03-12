# UnionIDSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** |  | 
**platform** | **str** |  | 
**two_factor_code** | **str** | 如果启用双因素认证登录，则必填 | [optional] 

## Example

```python
from PMCore.Client.models.union_id_sign_in_request import UnionIDSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnionIDSignInRequest from a JSON string
union_id_sign_in_request_instance = UnionIDSignInRequest.from_json(json)
# print the JSON string representation of the object
print(UnionIDSignInRequest.to_json())

# convert the object into a dict
union_id_sign_in_request_dict = union_id_sign_in_request_instance.to_dict()
# create an instance of UnionIDSignInRequest from a dict
union_id_sign_in_request_from_dict = UnionIDSignInRequest.from_dict(union_id_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


