# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**platform** | **str** |  | [optional] 
**union_id** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**pwd** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_is_valid** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**phone_is_valid** | **bool** |  | [optional] 
**relation_chain** | **str** |  | [optional] 
**interest_tags** | **str** |  | [optional] 
**biography** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**occupation** | **str** |  | [optional] 
**education** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**languages** | **str** |  | [optional] 
**social_links** | **str** |  | [optional] 
**relationship_status** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**company_position** | **str** |  | [optional] 
**private_settings** | **str** |  | [optional] 
**is_lock** | **bool** |  | [optional] 
**lock_until** | **datetime** |  | [optional] 
**enable_user_name_sign_in** | **bool** |  | [optional] 
**enable_email_sign_in** | **bool** |  | [optional] 
**enable_phone_sign_in** | **bool** |  | [optional] 
**enable_union_id_sign_in** | **bool** |  | [optional] 
**enable_o_auth** | **bool** |  | [optional] 
**enable2_fa_auth** | **bool** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from PMCore.Client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


