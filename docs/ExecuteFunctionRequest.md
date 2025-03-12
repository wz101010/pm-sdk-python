# ExecuteFunctionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_key** | **str** | 函数标识 | [optional] 

## Example

```python
from PMCore.Client.models.execute_function_request import ExecuteFunctionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteFunctionRequest from a JSON string
execute_function_request_instance = ExecuteFunctionRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteFunctionRequest.to_json())

# convert the object into a dict
execute_function_request_dict = execute_function_request_instance.to_dict()
# create an instance of ExecuteFunctionRequest from a dict
execute_function_request_from_dict = ExecuteFunctionRequest.from_dict(execute_function_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


