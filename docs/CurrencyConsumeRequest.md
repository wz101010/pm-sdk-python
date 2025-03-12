# CurrencyConsumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | 虚拟币代码 | 
**balance** | **int** | 消费额 | 
**remark** | **str** | 备注 | [optional] 
**description** | **str** | 描述 | [optional] 
**tags** | **str** | 标签 | [optional] 

## Example

```python
from PMCore.Client.models.currency_consume_request import CurrencyConsumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConsumeRequest from a JSON string
currency_consume_request_instance = CurrencyConsumeRequest.from_json(json)
# print the JSON string representation of the object
print(CurrencyConsumeRequest.to_json())

# convert the object into a dict
currency_consume_request_dict = currency_consume_request_instance.to_dict()
# create an instance of CurrencyConsumeRequest from a dict
currency_consume_request_from_dict = CurrencyConsumeRequest.from_dict(currency_consume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


