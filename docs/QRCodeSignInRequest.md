# QRCodeSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_key** | **int** |  | 

## Example

```python
from PMCore.Client.models.qr_code_sign_in_request import QRCodeSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QRCodeSignInRequest from a JSON string
qr_code_sign_in_request_instance = QRCodeSignInRequest.from_json(json)
# print the JSON string representation of the object
print(QRCodeSignInRequest.to_json())

# convert the object into a dict
qr_code_sign_in_request_dict = qr_code_sign_in_request_instance.to_dict()
# create an instance of QRCodeSignInRequest from a dict
qr_code_sign_in_request_from_dict = QRCodeSignInRequest.from_dict(qr_code_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


