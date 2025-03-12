# QRCodeScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_key** | **int** |  | 

## Example

```python
from PMCore.Client.models.qr_code_scan_request import QRCodeScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QRCodeScanRequest from a JSON string
qr_code_scan_request_instance = QRCodeScanRequest.from_json(json)
# print the JSON string representation of the object
print(QRCodeScanRequest.to_json())

# convert the object into a dict
qr_code_scan_request_dict = qr_code_scan_request_instance.to_dict()
# create an instance of QRCodeScanRequest from a dict
qr_code_scan_request_from_dict = QRCodeScanRequest.from_dict(qr_code_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


