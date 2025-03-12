# GeoLocationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | 纬度 | [optional] 
**longitude** | **float** | 经度 | [optional] 
**location_name** | **str** | 地点的名称 | [optional] 
**location_type** | **str** | 地点的类型，如家庭、工作、学校等 | [optional] 
**recipient_name** | **str** | 收货人姓名 | [optional] 
**phone_number** | **str** | 收货人联系电话 | [optional] 
**email** | **str** | 收货人电子邮件 | [optional] 
**country** | **str** | 国家 | [optional] 
**state** | **str** | 州/省 | [optional] 
**city** | **str** | 城市 | [optional] 
**district** | **str** | 区/县 | [optional] 
**street** | **str** | 街道 | [optional] 
**zip_code** | **str** | 邮政编码 | [optional] 
**address** | **str** | 详细的地址信息 | [optional] 
**map_type** | **str** | 地址类型，百度、高德、谷歌 | [optional] 
**remark** | **str** | 备注 | [optional] 
**tags** | **str** | 标签 | [optional] 
**enable** | **bool** | 启用 | [optional] 
**show_index** | **int** | 排序 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新的时间 | [optional] 

## Example

```python
from PMCore.Client.models.geo_location_model import GeoLocationModel

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocationModel from a JSON string
geo_location_model_instance = GeoLocationModel.from_json(json)
# print the JSON string representation of the object
print(GeoLocationModel.to_json())

# convert the object into a dict
geo_location_model_dict = geo_location_model_instance.to_dict()
# create an instance of GeoLocationModel from a dict
geo_location_model_from_dict = GeoLocationModel.from_dict(geo_location_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


