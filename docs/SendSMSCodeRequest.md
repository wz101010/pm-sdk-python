# SendSMSCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | 手机号 | 
**type** | **str** | 用途。可选值：signup/forgetpwd | 

## Example

```python
from PMCore.Client.models.send_sms_code_request import SendSMSCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendSMSCodeRequest from a JSON string
send_sms_code_request_instance = SendSMSCodeRequest.from_json(json)
# print the JSON string representation of the object
print(SendSMSCodeRequest.to_json())

# convert the object into a dict
send_sms_code_request_dict = send_sms_code_request_instance.to_dict()
# create an instance of SendSMSCodeRequest from a dict
send_sms_code_request_from_dict = SendSMSCodeRequest.from_dict(send_sms_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


