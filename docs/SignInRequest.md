# SignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | 
**pwd** | **str** |  | 
**two_factor_code** | **str** | 如果启用双因素认证登录，则必填 | [optional] 

## Example

```python
from PMCore.Client.models.sign_in_request import SignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignInRequest from a JSON string
sign_in_request_instance = SignInRequest.from_json(json)
# print the JSON string representation of the object
print(SignInRequest.to_json())

# convert the object into a dict
sign_in_request_dict = sign_in_request_instance.to_dict()
# create an instance of SignInRequest from a dict
sign_in_request_from_dict = SignInRequest.from_dict(sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


