# RechargePointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | 虚拟币代码 | 
**balance** | **int** | 充值额 | 
**remark** | **str** | 备注 | [optional] 
**description** | **str** | 描述 | [optional] 
**tags** | **str** | 标签 | [optional] 

## Example

```python
from PMCore.Client.models.recharge_point_request import RechargePointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RechargePointRequest from a JSON string
recharge_point_request_instance = RechargePointRequest.from_json(json)
# print the JSON string representation of the object
print(RechargePointRequest.to_json())

# convert the object into a dict
recharge_point_request_dict = recharge_point_request_instance.to_dict()
# create an instance of RechargePointRequest from a dict
recharge_point_request_from_dict = RechargePointRequest.from_dict(recharge_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


