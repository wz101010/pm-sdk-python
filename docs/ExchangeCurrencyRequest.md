# ExchangeCurrencyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_currency** | **str** | 源虚拟币代码 | 
**currency** | **str** | 目标虚拟币代码 | 
**balance** | **int** | 兑换额 | 
**remark** | **str** | 备注 | [optional] 
**description** | **str** | 描述 | [optional] 
**tags** | **str** | 标签 | [optional] 

## Example

```python
from PMCore.Client.models.exchange_currency_request import ExchangeCurrencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeCurrencyRequest from a JSON string
exchange_currency_request_instance = ExchangeCurrencyRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeCurrencyRequest.to_json())

# convert the object into a dict
exchange_currency_request_dict = exchange_currency_request_instance.to_dict()
# create an instance of ExchangeCurrencyRequest from a dict
exchange_currency_request_from_dict = ExchangeCurrencyRequest.from_dict(exchange_currency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


