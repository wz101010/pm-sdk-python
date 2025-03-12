# EmailSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**pwd** | **str** |  | 
**email_code** | **str** | 邮箱验证码 | [optional] 
**phone** | **str** | 手机号 | [optional] 
**phone_code** | **str** | 手机验证码（只有启用的手机验证码功能时，才需要传入） | [optional] 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 
**data** | **str** | 自定义数据 | [optional] 

## Example

```python
from PMCore.Client.models.email_sign_up_request import EmailSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSignUpRequest from a JSON string
email_sign_up_request_instance = EmailSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(EmailSignUpRequest.to_json())

# convert the object into a dict
email_sign_up_request_dict = email_sign_up_request_instance.to_dict()
# create an instance of EmailSignUpRequest from a dict
email_sign_up_request_from_dict = EmailSignUpRequest.from_dict(email_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


