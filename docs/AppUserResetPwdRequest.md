# AppUserResetPwdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**code** | **str** |  | 
**pwd** | **str** |  | 

## Example

```python
from PMCore.Client.models.app_user_reset_pwd_request import AppUserResetPwdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserResetPwdRequest from a JSON string
app_user_reset_pwd_request_instance = AppUserResetPwdRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserResetPwdRequest.to_json())

# convert the object into a dict
app_user_reset_pwd_request_dict = app_user_reset_pwd_request_instance.to_dict()
# create an instance of AppUserResetPwdRequest from a dict
app_user_reset_pwd_request_from_dict = AppUserResetPwdRequest.from_dict(app_user_reset_pwd_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


