# UnionIDSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | 登录账号，可空 | [optional] 
**union_id** | **str** | UnionID | 
**platform** | **str** | 平台标识 | 
**pwd** | **str** | 密码，6~32位 | 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 
**data** | **str** | 自定义数据 | [optional] 
**email** | **str** | 邮箱 | [optional] 
**email_code** | **str** | 邮箱验证码（只有启用的邮箱验证码功能时，才需要传入） | [optional] 
**phone** | **str** | 手机号 | [optional] 
**phone_code** | **str** | 手机验证码（只有启用的手机验证码功能时，才需要传入） | [optional] 

## Example

```python
from PMCore.Client.models.union_id_sign_up_request import UnionIDSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnionIDSignUpRequest from a JSON string
union_id_sign_up_request_instance = UnionIDSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(UnionIDSignUpRequest.to_json())

# convert the object into a dict
union_id_sign_up_request_dict = union_id_sign_up_request_instance.to_dict()
# create an instance of UnionIDSignUpRequest from a dict
union_id_sign_up_request_from_dict = UnionIDSignUpRequest.from_dict(union_id_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


