# PhoneSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 
**verify_code** | **str** |  | 
**two_factor_code** | **str** | 如果启用双因素认证登录，则必填 | [optional] 

## Example

```python
from PMCore.Client.models.phone_sign_in_request import PhoneSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneSignInRequest from a JSON string
phone_sign_in_request_instance = PhoneSignInRequest.from_json(json)
# print the JSON string representation of the object
print(PhoneSignInRequest.to_json())

# convert the object into a dict
phone_sign_in_request_dict = phone_sign_in_request_instance.to_dict()
# create an instance of PhoneSignInRequest from a dict
phone_sign_in_request_from_dict = PhoneSignInRequest.from_dict(phone_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


