# OAuthAccountSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** |  | 
**platform** | **str** |  | 
**two_factor_code** | **str** | 如果启用双因素认证登录，则必填 | [optional] 

## Example

```python
from PMCore.Client.models.o_auth_account_sign_in_request import OAuthAccountSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAccountSignInRequest from a JSON string
o_auth_account_sign_in_request_instance = OAuthAccountSignInRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthAccountSignInRequest.to_json())

# convert the object into a dict
o_auth_account_sign_in_request_dict = o_auth_account_sign_in_request_instance.to_dict()
# create an instance of OAuthAccountSignInRequest from a dict
o_auth_account_sign_in_request_from_dict = OAuthAccountSignInRequest.from_dict(o_auth_account_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


