# ReturnPageNotifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**auth_app_id** | **str** |  | [optional] 
**charset** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**out_trade_no** | **str** |  | [optional] 
**seller_id** | **str** |  | [optional] 
**sign** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**total_amount** | **str** |  | [optional] 
**trade_no** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.return_page_notify_request import ReturnPageNotifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPageNotifyRequest from a JSON string
return_page_notify_request_instance = ReturnPageNotifyRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnPageNotifyRequest.to_json())

# convert the object into a dict
return_page_notify_request_dict = return_page_notify_request_instance.to_dict()
# create an instance of ReturnPageNotifyRequest from a dict
return_page_notify_request_from_dict = ReturnPageNotifyRequest.from_dict(return_page_notify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


