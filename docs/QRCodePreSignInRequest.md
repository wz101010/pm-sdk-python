# QRCodePreSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**scheme** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.qr_code_pre_sign_in_request import QRCodePreSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QRCodePreSignInRequest from a JSON string
qr_code_pre_sign_in_request_instance = QRCodePreSignInRequest.from_json(json)
# print the JSON string representation of the object
print(QRCodePreSignInRequest.to_json())

# convert the object into a dict
qr_code_pre_sign_in_request_dict = qr_code_pre_sign_in_request_instance.to_dict()
# create an instance of QRCodePreSignInRequest from a dict
qr_code_pre_sign_in_request_from_dict = QRCodePreSignInRequest.from_dict(qr_code_pre_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


