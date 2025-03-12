# PostIndexRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **Dict[str, List[object]]** |  | 
**options** | **Dict[str, List[object]]** |  | [optional] 

## Example

```python
from PMCore.Client.models.post_index_request import PostIndexRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostIndexRequest from a JSON string
post_index_request_instance = PostIndexRequest.from_json(json)
# print the JSON string representation of the object
print(PostIndexRequest.to_json())

# convert the object into a dict
post_index_request_dict = post_index_request_instance.to_dict()
# create an instance of PostIndexRequest from a dict
post_index_request_from_dict = PostIndexRequest.from_dict(post_index_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


