# Currency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**currency_type** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**enable_virtual_recharge** | **bool** |  | [optional] 
**enable_virtual_consume** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**fiat_exchange_rate** | **int** |  | [optional] 
**fiat_daily_recharge_limit** | **int** |  | [optional] 
**total_supply** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


