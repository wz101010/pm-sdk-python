# AlipayCreateOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** | 自定义订单号 | 
**amount** | **float** | 订单金额。例如：0.01 | 
**subject** | **str** | 商品名称 | 
**return_url** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.alipay_create_order_request import AlipayCreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayCreateOrderRequest from a JSON string
alipay_create_order_request_instance = AlipayCreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AlipayCreateOrderRequest.to_json())

# convert the object into a dict
alipay_create_order_request_dict = alipay_create_order_request_instance.to_dict()
# create an instance of AlipayCreateOrderRequest from a dict
alipay_create_order_request_from_dict = AlipayCreateOrderRequest.from_dict(alipay_create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


