# FollowerPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**closeness_score** | **int** |  | [optional] 
**attention_score** | **int** |  | [optional] 
**tags** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 

## Example

```python
from PMCore.Client.models.follower_put_model import FollowerPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of FollowerPutModel from a JSON string
follower_put_model_instance = FollowerPutModel.from_json(json)
# print the JSON string representation of the object
print(FollowerPutModel.to_json())

# convert the object into a dict
follower_put_model_dict = follower_put_model_instance.to_dict()
# create an instance of FollowerPutModel from a dict
follower_put_model_from_dict = FollowerPutModel.from_dict(follower_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


