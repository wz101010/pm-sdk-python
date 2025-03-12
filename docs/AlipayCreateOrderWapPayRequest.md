# AlipayCreateOrderWapPayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** | 自定义订单号 | 
**amount** | **float** | 订单金额。例如：0.01 | 
**subject** | **str** | 商品名称 | 
**return_url** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.alipay_create_order_wap_pay_request import AlipayCreateOrderWapPayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayCreateOrderWapPayRequest from a JSON string
alipay_create_order_wap_pay_request_instance = AlipayCreateOrderWapPayRequest.from_json(json)
# print the JSON string representation of the object
print(AlipayCreateOrderWapPayRequest.to_json())

# convert the object into a dict
alipay_create_order_wap_pay_request_dict = alipay_create_order_wap_pay_request_instance.to_dict()
# create an instance of AlipayCreateOrderWapPayRequest from a dict
alipay_create_order_wap_pay_request_from_dict = AlipayCreateOrderWapPayRequest.from_dict(alipay_create_order_wap_pay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


