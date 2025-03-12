# GrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** | 返回地址。默认无限制，也可在【安全-开放认证网址白名单】配置 | [optional] 
**grant_type** | **str** | 授权类型。可选：email、phone、unionid、account | 
**scopes** | **str** | 自定义授权范围，用英文空格分隔 | 
**user_name** | **str** | 用户名。授权类型为：email/phone/account必填 | [optional] 
**password** | **str** | 登录密码。授权类型为：email/phone/account必填 | [optional] 
**union_id** | **str** | unionId。授权类型为：unionid必填 | [optional] 
**platform** | **str** | 平台。授权类型为：unionid必填 | [optional] 
**expire_in_days** | **int** | 授权有效期。1~99天 | [optional] 

## Example

```python
from PMCore.Client.models.grant_request import GrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantRequest from a JSON string
grant_request_instance = GrantRequest.from_json(json)
# print the JSON string representation of the object
print(GrantRequest.to_json())

# convert the object into a dict
grant_request_dict = grant_request_instance.to_dict()
# create an instance of GrantRequest from a dict
grant_request_from_dict = GrantRequest.from_dict(grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


