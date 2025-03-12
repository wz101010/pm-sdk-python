# PMCore.Client.UserSettingApi

All URIs are relative to *https://api-staging.paomo.fun*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_setting**](UserSettingApi.md#user_setting) | **GET** /UserSetting/{appKey}/{id} | 用户配置项详情
[**user_setting_delete**](UserSettingApi.md#user_setting_delete) | **DELETE** /UserSetting/{appKey}/{id} | 删除用户配置项
[**user_setting_post**](UserSettingApi.md#user_setting_post) | **POST** /UserSetting/{appKey} | 添加用户配置项
[**user_setting_put**](UserSettingApi.md#user_setting_put) | **PUT** /UserSetting/{appKey}/{id} | 更新用户配置项
[**user_settings**](UserSettingApi.md#user_settings) | **GET** /UserSetting/{appKey} | 用户配置列表


# **user_setting**
> JObjectApiResult user_setting(id, app_key)

用户配置项详情

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
    api_instance = PMCore.Client.UserSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 用户配置项详情
        api_response = api_instance.user_setting(id, app_key)
        print("The response of UserSettingApi->user_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingApi->user_setting: %s\n" % e)
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

# **user_setting_delete**
> JObjectApiResult user_setting_delete(id, app_key)

删除用户配置项

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
    api_instance = PMCore.Client.UserSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除用户配置项
        api_response = api_instance.user_setting_delete(id, app_key)
        print("The response of UserSettingApi->user_setting_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingApi->user_setting_delete: %s\n" % e)
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

# **user_setting_post**
> JObjectApiResult user_setting_post(app_key, user_setting=user_setting)

添加用户配置项

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.user_setting import UserSetting
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
    api_instance = PMCore.Client.UserSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    user_setting = PMCore.Client.UserSetting() # UserSetting |  (optional)

    try:
        # 添加用户配置项
        api_response = api_instance.user_setting_post(app_key, user_setting=user_setting)
        print("The response of UserSettingApi->user_setting_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingApi->user_setting_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_setting** | [**UserSetting**](UserSetting.md)|  | [optional] 

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

# **user_setting_put**
> JObjectApiResult user_setting_put(id, app_key, user_setting=user_setting)

更新用户配置项

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.user_setting import UserSetting
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
    api_instance = PMCore.Client.UserSettingApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    user_setting = PMCore.Client.UserSetting() # UserSetting |  (optional)

    try:
        # 更新用户配置项
        api_response = api_instance.user_setting_put(id, app_key, user_setting=user_setting)
        print("The response of UserSettingApi->user_setting_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingApi->user_setting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **user_setting** | [**UserSetting**](UserSetting.md)|  | [optional] 

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

# **user_settings**
> JObjectApiResult user_settings(app_key, user_id=user_id, code=code, tag=tag)

用户配置列表

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
    api_instance = PMCore.Client.UserSettingApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 56 # int |  (optional)
    code = 'code_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)

    try:
        # 用户配置列表
        api_response = api_instance.user_settings(app_key, user_id=user_id, code=code, tag=tag)
        print("The response of UserSettingApi->user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingApi->user_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **int**|  | [optional] 
 **code** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 

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

