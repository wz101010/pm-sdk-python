# PMCore.Client.AppSettingApi

All URIs are relative to *https://api-staging.paomo.fun*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_service_setting_group**](AppSettingApi.md#app_service_setting_group) | **GET** /AppSetting/{appKey}/Groups/{id} | 服务分组详情
[**app_service_setting_group_delete**](AppSettingApi.md#app_service_setting_group_delete) | **DELETE** /AppSetting/{appKey}/Groups/{id} | 删除服务分组
[**app_service_setting_group_post**](AppSettingApi.md#app_service_setting_group_post) | **POST** /AppSetting/{appKey}/Groups | 添加服务分组
[**app_service_setting_group_put**](AppSettingApi.md#app_service_setting_group_put) | **PUT** /AppSetting/{appKey}/Groups/{id} | 更新服务分组
[**app_service_setting_groups**](AppSettingApi.md#app_service_setting_groups) | **GET** /AppSetting/{appKey}/Groups | 服务分组
[**app_service_setting_item**](AppSettingApi.md#app_service_setting_item) | **GET** /AppSetting/{appKey}/Items/{id} | 服务配置项详情
[**app_service_setting_item_delete**](AppSettingApi.md#app_service_setting_item_delete) | **DELETE** /AppSetting/{appKey}/Items/{id} | 删除服务配置项
[**app_service_setting_item_post**](AppSettingApi.md#app_service_setting_item_post) | **POST** /AppSetting/{appKey}/Items | 添加服务配置项
[**app_service_setting_item_put**](AppSettingApi.md#app_service_setting_item_put) | **PUT** /AppSetting/{appKey}/Items/{id} | 更新服务配置项
[**app_service_setting_items**](AppSettingApi.md#app_service_setting_items) | **GET** /AppSetting/{appKey}/Items | 服务配置项列表
[**app_service_setting_provider**](AppSettingApi.md#app_service_setting_provider) | **GET** /AppSetting/{appKey}/Providers/{id} | 服务商详情
[**app_service_setting_provider_delete**](AppSettingApi.md#app_service_setting_provider_delete) | **DELETE** /AppSetting/{appKey}/Providers/{id} | 删除服务商
[**app_service_setting_provider_post**](AppSettingApi.md#app_service_setting_provider_post) | **POST** /AppSetting/{appKey}/Providers | 添加服务商
[**app_service_setting_provider_put**](AppSettingApi.md#app_service_setting_provider_put) | **PUT** /AppSetting/{appKey}/Providers/{id} | 更新服务商
[**app_service_setting_providers**](AppSettingApi.md#app_service_setting_providers) | **GET** /AppSetting/{appKey}/Providers | 服务商列表
[**app_setting**](AppSettingApi.md#app_setting) | **GET** /AppSetting/{appKey}/{id} | 配置详情
[**app_setting_delete**](AppSettingApi.md#app_setting_delete) | **DELETE** /AppSetting/{appKey}/{id} | 删除配置
[**app_setting_post**](AppSettingApi.md#app_setting_post) | **POST** /AppSetting/{appKey} | 增加配置
[**app_setting_put**](AppSettingApi.md#app_setting_put) | **PUT** /AppSetting/{appKey}/{id} | 更新配置
[**app_settings**](AppSettingApi.md#app_settings) | **GET** /AppSetting/{appKey} | 配置列表


# **app_service_setting_group**
> JObjectApiResult app_service_setting_group(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 服务分组详情
        api_response = api_instance.app_service_setting_group(id, app_key)
        print("The response of AppSettingApi->app_service_setting_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_group_delete**
> JObjectApiResult app_service_setting_group_delete(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除服务分组
        api_response = api_instance.app_service_setting_group_delete(id, app_key)
        print("The response of AppSettingApi->app_service_setting_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_group_post**
> JObjectApiResult app_service_setting_group_post(app_key, service_group=service_group)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    service_group = PMCore.Client.ServiceGroup() # ServiceGroup |  (optional)

    try:
        # 添加服务分组
        api_response = api_instance.app_service_setting_group_post(app_key, service_group=service_group)
        print("The response of AppSettingApi->app_service_setting_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_service_setting_group_put**
> JObjectApiResult app_service_setting_group_put(id, app_key, service_group=service_group)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    service_group = PMCore.Client.ServiceGroup() # ServiceGroup |  (optional)

    try:
        # 更新服务分组
        api_response = api_instance.app_service_setting_group_put(id, app_key, service_group=service_group)
        print("The response of AppSettingApi->app_service_setting_group_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_group_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
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

# **app_service_setting_groups**
> JObjectApiResult app_service_setting_groups(app_key, provider_id=provider_id, show_flag=show_flag)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    provider_id = 56 # int |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务分组
        api_response = api_instance.app_service_setting_groups(app_key, provider_id=provider_id, show_flag=show_flag)
        print("The response of AppSettingApi->app_service_setting_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_service_setting_item**
> JObjectApiResult app_service_setting_item(id, app_key)

服务配置项详情

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 服务配置项详情
        api_response = api_instance.app_service_setting_item(id, app_key)
        print("The response of AppSettingApi->app_service_setting_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_item_delete**
> JObjectApiResult app_service_setting_item_delete(id, app_key)

删除服务配置项

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除服务配置项
        api_response = api_instance.app_service_setting_item_delete(id, app_key)
        print("The response of AppSettingApi->app_service_setting_item_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_item_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_item_post**
> JObjectApiResult app_service_setting_item_post(app_key, service_item=service_item)

添加服务配置项

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    service_item = PMCore.Client.ServiceItem() # ServiceItem |  (optional)

    try:
        # 添加服务配置项
        api_response = api_instance.app_service_setting_item_post(app_key, service_item=service_item)
        print("The response of AppSettingApi->app_service_setting_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_service_setting_item_put**
> JObjectApiResult app_service_setting_item_put(id, app_key, service_item=service_item)

更新服务配置项

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    service_item = PMCore.Client.ServiceItem() # ServiceItem |  (optional)

    try:
        # 更新服务配置项
        api_response = api_instance.app_service_setting_item_put(id, app_key, service_item=service_item)
        print("The response of AppSettingApi->app_service_setting_item_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_item_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
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

# **app_service_setting_items**
> JObjectApiResult app_service_setting_items(app_key, biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)

服务配置项列表

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    biz_code = 'biz_code_example' # str |  (optional)
    provider_code = 'provider_code_example' # str |  (optional)
    group_code = 'group_code_example' # str |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务配置项列表
        api_response = api_instance.app_service_setting_items(app_key, biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)
        print("The response of AppSettingApi->app_service_setting_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_service_setting_provider**
> JObjectApiResult app_service_setting_provider(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 服务商详情
        api_response = api_instance.app_service_setting_provider(id, app_key)
        print("The response of AppSettingApi->app_service_setting_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_provider_delete**
> JObjectApiResult app_service_setting_provider_delete(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除服务商
        api_response = api_instance.app_service_setting_provider_delete(id, app_key)
        print("The response of AppSettingApi->app_service_setting_provider_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_provider_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_service_setting_provider_post**
> JObjectApiResult app_service_setting_provider_post(app_key, service_provider=service_provider)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    service_provider = PMCore.Client.ServiceProvider() # ServiceProvider |  (optional)

    try:
        # 添加服务商
        api_response = api_instance.app_service_setting_provider_post(app_key, service_provider=service_provider)
        print("The response of AppSettingApi->app_service_setting_provider_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_provider_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_service_setting_provider_put**
> JObjectApiResult app_service_setting_provider_put(id, app_key, service_provider=service_provider)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    service_provider = PMCore.Client.ServiceProvider() # ServiceProvider |  (optional)

    try:
        # 更新服务商
        api_response = api_instance.app_service_setting_provider_put(id, app_key, service_provider=service_provider)
        print("The response of AppSettingApi->app_service_setting_provider_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_provider_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
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

# **app_service_setting_providers**
> JObjectApiResult app_service_setting_providers(app_key, biz_code=biz_code, show_flag=show_flag)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    biz_code = 'biz_code_example' # str |  (optional)
    show_flag = False # bool |  (optional) (default to False)

    try:
        # 服务商列表
        api_response = api_instance.app_service_setting_providers(app_key, biz_code=biz_code, show_flag=show_flag)
        print("The response of AppSettingApi->app_service_setting_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_service_setting_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_setting**
> JObjectApiResult app_setting(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 配置详情
        api_response = api_instance.app_setting(id, app_key)
        print("The response of AppSettingApi->app_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_setting_delete**
> JObjectApiResult app_setting_delete(id, app_key)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除配置
        api_response = api_instance.app_setting_delete(id, app_key)
        print("The response of AppSettingApi->app_setting_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_setting_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 

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

# **app_setting_post**
> JObjectApiResult app_setting_post(app_key, app_setting=app_setting)

增加配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.app_setting import AppSetting
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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    app_setting = PMCore.Client.AppSetting() # AppSetting |  (optional)

    try:
        # 增加配置
        api_response = api_instance.app_setting_post(app_key, app_setting=app_setting)
        print("The response of AppSettingApi->app_setting_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_setting_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app_setting** | [**AppSetting**](AppSetting.md)|  | [optional] 

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

# **app_setting_put**
> JObjectApiResult app_setting_put(id, app_key, app_setting=app_setting)

更新配置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.app_setting import AppSetting
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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    app_setting = PMCore.Client.AppSetting() # AppSetting |  (optional)

    try:
        # 更新配置
        api_response = api_instance.app_setting_put(id, app_key, app_setting=app_setting)
        print("The response of AppSettingApi->app_setting_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_setting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **app_setting** | [**AppSetting**](AppSetting.md)|  | [optional] 

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

# **app_settings**
> JObjectApiResult app_settings(app_key, provider_code=provider_code, group_code=group_code, tag=tag, code=code)

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
    api_instance = PMCore.Client.AppSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    provider_code = 'provider_code_example' # str | 服务商代码 (optional)
    group_code = 'group_code_example' # str | 服务代码 (optional)
    tag = 'tag_example' # str | 标签 (optional)
    code = 'code_example' # str | 配置项代码 (optional)

    try:
        # 配置列表
        api_response = api_instance.app_settings(app_key, provider_code=provider_code, group_code=group_code, tag=tag, code=code)
        print("The response of AppSettingApi->app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingApi->app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **provider_code** | **str**| 服务商代码 | [optional] 
 **group_code** | **str**| 服务代码 | [optional] 
 **tag** | **str**| 标签 | [optional] 
 **code** | **str**| 配置项代码 | [optional] 

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

