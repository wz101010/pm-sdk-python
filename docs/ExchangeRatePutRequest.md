# ExchangeRatePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_currency_code** | **str** |  | [optional] 
**exchange_rate** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.exchange_rate_put_request import ExchangeRatePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRatePutRequest from a JSON string
exchange_rate_put_request_instance = ExchangeRatePutRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeRatePutRequest.to_json())

# convert the object into a dict
exchange_rate_put_request_dict = exchange_rate_put_request_instance.to_dict()
# create an instance of ExchangeRatePutRequest from a dict
exchange_rate_put_request_from_dict = ExchangeRatePutRequest.from_dict(exchange_rate_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


