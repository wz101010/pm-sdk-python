# PMCore.Client.ServiceSettingApi

All URIs are relative to *https://api-staging.paomo.fun*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_setting**](ServiceSettingApi.md#service_setting) | **GET** /ServiceSetting/{id} | 配置详情
[**service_setting_delete**](ServiceSettingApi.md#service_setting_delete) | **DELETE** /ServiceSetting/{id} | 删除配置
[**service_setting_group**](ServiceSettingApi.md#service_setting_group) | **GET** /ServiceSetting/Groups/{id} | 服务分组详情
[**service_setting_group_delete**](ServiceSettingApi.md#service_setting_group_delete) | **DELETE** /ServiceSetting/Groups/{id} | 删除服务分组
[**service_setting_group_post**](ServiceSettingApi.md#service_setting_group_post) | **POST** /ServiceSetting/Groups | 添加服务分组
[**service_setting_group_put**](ServiceSettingApi.md#service_setting_group_put) | **PUT** /ServiceSetting/Groups/{id} | 更新服务分组
[**service_setting_groups**](ServiceSettingApi.md#service_setting_groups) | **GET** /ServiceSetting/Groups | 服务分组
[**service_setting_item**](ServiceSettingApi.md#service_setting_item) | **GET** /ServiceSetting/Items/{id} | 服务配置详情
[**service_setting_item_delete**](ServiceSettingApi.md#service_setting_item_delete) | **DELETE** /ServiceSetting/Items/{id} | 删除服务配置
[**service_setting_item_post**](ServiceSettingApi.md#service_setting_item_post) | **POST** /ServiceSetting/Items | 添加服务配置
[**service_setting_item_put**](ServiceSettingApi.md#service_setting_item_put) | **PUT** /ServiceSetting/Items/{id} | 更新服务配置
[**service_setting_items**](ServiceSettingApi.md#service_setting_items) | **GET** /ServiceSetting/Items | 服务配置列表
[**service_setting_post**](ServiceSettingApi.md#service_setting_post) | **POST** /ServiceSetting | 增加配置
[**service_setting_provider**](ServiceSettingApi.md#service_setting_provider) | **GET** /ServiceSetting/Providers/{id} | 服务商详情
[**service_setting_provider_delete**](ServiceSettingApi.md#service_setting_provider_delete) | **DELETE** /ServiceSetting/Providers/{id} | 删除服务商
[**service_setting_provider_post**](ServiceSettingApi.md#service_setting_provider_post) | **POST** /ServiceSetting/Providers | 添加服务商
[**service_setting_provider_put**](ServiceSettingApi.md#service_setting_provider_put) | **PUT** /ServiceSetting/Providers/{id} | 更新服务商
[**service_setting_providers**](ServiceSettingApi.md#service_setting_providers) | **GET** /ServiceSetting/Providers | 服务商列表
[**service_setting_put**](ServiceSettingApi.md#service_setting_put) | **PUT** /ServiceSetting/{id} | 更新配置
[**service_settings**](ServiceSettingApi.md#service_settings) | **GET** /ServiceSetting | 配置列表


# **service_setting**
> JObjectApiResult service_setting(id)

配置详情

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 配置详情
        api_response = api_instance.service_setting(id)
        print("The response of ServiceSettingApi->service_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_delete**
> JObjectApiResult service_setting_delete(id)

删除配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 删除配置
        api_response = api_instance.service_setting_delete(id)
        print("The response of ServiceSettingApi->service_setting_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_group**
> JObjectApiResult service_setting_group(id)

服务分组详情

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 服务分组详情
        api_response = api_instance.service_setting_group(id)
        print("The response of ServiceSettingApi->service_setting_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_group_delete**
> JObjectApiResult service_setting_group_delete(id)

删除服务分组

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 删除服务分组
        api_response = api_instance.service_setting_group_delete(id)
        print("The response of ServiceSettingApi->service_setting_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_group_post**
> JObjectApiResult service_setting_group_post(service_group=service_group)

添加服务分组

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_group import ServiceGroup
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    service_group = PMCore.Client.ServiceGroup() # ServiceGroup |  (optional)

    try:
        # 添加服务分组
        api_response = api_instance.service_setting_group_post(service_group=service_group)
        print("The response of ServiceSettingApi->service_setting_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group** | [**ServiceGroup**](ServiceGroup.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_group_put**
> JObjectApiResult service_setting_group_put(id, service_group=service_group)

更新服务分组

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_group import ServiceGroup
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 
    service_group = PMCore.Client.ServiceGroup() # ServiceGroup |  (optional)

    try:
        # 更新服务分组
        api_response = api_instance.service_setting_group_put(id, service_group=service_group)
        print("The response of ServiceSettingApi->service_setting_group_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **service_group** | [**ServiceGroup**](ServiceGroup.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_groups**
> JObjectApiResult service_setting_groups(provider_id=provider_id, show_flag=show_flag)

服务分组

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    provider_id = 56 # int |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务分组
        api_response = api_instance.service_setting_groups(provider_id=provider_id, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**|  | [optional] 
 **show_flag** | **bool**|  | [optional] [default to False]

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_item**
> JObjectApiResult service_setting_item(id)

服务配置详情

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 服务配置详情
        api_response = api_instance.service_setting_item(id)
        print("The response of ServiceSettingApi->service_setting_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_item_delete**
> JObjectApiResult service_setting_item_delete(id)

删除服务配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 删除服务配置
        api_response = api_instance.service_setting_item_delete(id)
        print("The response of ServiceSettingApi->service_setting_item_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_item_post**
> JObjectApiResult service_setting_item_post(service_item=service_item)

添加服务配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_item import ServiceItem
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    service_item = PMCore.Client.ServiceItem() # ServiceItem |  (optional)

    try:
        # 添加服务配置
        api_response = api_instance.service_setting_item_post(service_item=service_item)
        print("The response of ServiceSettingApi->service_setting_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_item** | [**ServiceItem**](ServiceItem.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_item_put**
> JObjectApiResult service_setting_item_put(id, service_item=service_item)

更新服务配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_item import ServiceItem
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 
    service_item = PMCore.Client.ServiceItem() # ServiceItem |  (optional)

    try:
        # 更新服务配置
        api_response = api_instance.service_setting_item_put(id, service_item=service_item)
        print("The response of ServiceSettingApi->service_setting_item_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **service_item** | [**ServiceItem**](ServiceItem.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_items**
> JObjectApiResult service_setting_items(biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)

服务配置列表

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str |  (optional)
    provider_code = 'provider_code_example' # str |  (optional)
    group_code = 'group_code_example' # str |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务配置列表
        api_response = api_instance.service_setting_items(biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**|  | [optional] 
 **provider_code** | **str**|  | [optional] 
 **group_code** | **str**|  | [optional] 
 **show_flag** | **bool**|  | [optional] [default to False]

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_post**
> JObjectApiResult service_setting_post(settings=settings)

增加配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.settings import Settings
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    settings = PMCore.Client.Settings() # Settings |  (optional)

    try:
        # 增加配置
        api_response = api_instance.service_setting_post(settings=settings)
        print("The response of ServiceSettingApi->service_setting_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**Settings**](Settings.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_provider**
> JObjectApiResult service_setting_provider(id)

服务商详情

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 服务商详情
        api_response = api_instance.service_setting_provider(id)
        print("The response of ServiceSettingApi->service_setting_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_provider_delete**
> JObjectApiResult service_setting_provider_delete(id)

删除服务商

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 

    try:
        # 删除服务商
        api_response = api_instance.service_setting_provider_delete(id)
        print("The response of ServiceSettingApi->service_setting_provider_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_provider_post**
> JObjectApiResult service_setting_provider_post(service_provider=service_provider)

添加服务商

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_provider import ServiceProvider
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    service_provider = PMCore.Client.ServiceProvider() # ServiceProvider |  (optional)

    try:
        # 添加服务商
        api_response = api_instance.service_setting_provider_post(service_provider=service_provider)
        print("The response of ServiceSettingApi->service_setting_provider_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider** | [**ServiceProvider**](ServiceProvider.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_provider_put**
> JObjectApiResult service_setting_provider_put(id, service_provider=service_provider)

更新服务商

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.service_provider import ServiceProvider
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 
    service_provider = PMCore.Client.ServiceProvider() # ServiceProvider |  (optional)

    try:
        # 更新服务商
        api_response = api_instance.service_setting_provider_put(id, service_provider=service_provider)
        print("The response of ServiceSettingApi->service_setting_provider_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **service_provider** | [**ServiceProvider**](ServiceProvider.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_providers**
> JObjectApiResult service_setting_providers(biz_code=biz_code, show_flag=show_flag)

服务商列表

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务商列表
        api_response = api_instance.service_setting_providers(biz_code=biz_code, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**|  | [optional] 
 **show_flag** | **bool**|  | [optional] [default to False]

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_setting_put**
> JObjectApiResult service_setting_put(id, settings=settings)

更新配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.settings import Settings
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    id = 56 # int | 
    settings = PMCore.Client.Settings() # Settings |  (optional)

    try:
        # 更新配置
        api_response = api_instance.service_setting_put(id, settings=settings)
        print("The response of ServiceSettingApi->service_setting_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **settings** | [**Settings**](Settings.md)|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_settings**
> JObjectApiResult service_settings(biz_code, biz_id, provider_code=provider_code, group_code=group_code, tag=tag, code=code)

配置列表

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.paomo.fun
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://api-staging.paomo.fun"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str | 
    biz_id = 'biz_id_example' # str | 
    provider_code = 'provider_code_example' # str |  (optional)
    group_code = 'group_code_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    code = 'code_example' # str |  (optional)

    try:
        # 配置列表
        api_response = api_instance.service_settings(biz_code, biz_id, provider_code=provider_code, group_code=group_code, tag=tag, code=code)
        print("The response of ServiceSettingApi->service_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**|  | 
 **biz_id** | **str**|  | 
 **provider_code** | **str**|  | [optional] 
 **group_code** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

