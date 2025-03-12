# AccessTokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**tags** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**permissions** | **str** |  | [optional] 
**expire_in_days** | **int** |  | [optional] 

## Example

```python
from PMCore.Client.models.access_token_post_request import AccessTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenPostRequest from a JSON string
access_token_post_request_instance = AccessTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokenPostRequest.to_json())

# convert the object into a dict
access_token_post_request_dict = access_token_post_request_instance.to_dict()
# create an instance of AccessTokenPostRequest from a dict
access_token_post_request_from_dict = AccessTokenPostRequest.from_dict(access_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


