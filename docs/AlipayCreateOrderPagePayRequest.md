# AlipayCreateOrderPagePayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** | 自定义订单号 | 
**amount** | **float** | 订单金额。例如：0.01 | 
**subject** | **str** | 商品名称 | 
**return_url** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.alipay_create_order_page_pay_request import AlipayCreateOrderPagePayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayCreateOrderPagePayRequest from a JSON string
alipay_create_order_page_pay_request_instance = AlipayCreateOrderPagePayRequest.from_json(json)
# print the JSON string representation of the object
print(AlipayCreateOrderPagePayRequest.to_json())

# convert the object into a dict
alipay_create_order_page_pay_request_dict = alipay_create_order_page_pay_request_instance.to_dict()
# create an instance of AlipayCreateOrderPagePayRequest from a dict
alipay_create_order_page_pay_request_from_dict = AlipayCreateOrderPagePayRequest.from_dict(alipay_create_order_page_pay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


