# PMCore.Client.AppApi

All URIs are relative to *https://api-staging.paomo.fun*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app**](AppApi.md#app) | **GET** /App/{appKey} | 应用详情
[**app2_fa**](AppApi.md#app2_fa) | **GET** /App/{appKey}/2FA | 双因素验证 获取
[**app2_fa_check**](AppApi.md#app2_fa_check) | **GET** /App/{appKey}/2FACheck | 双因素验证 验证
[**app_check_version**](AppApi.md#app_check_version) | **GET** /App/{appKey}/CheckVersion | 更新应用数据库
[**app_delete**](AppApi.md#app_delete) | **DELETE** /App/{appKey} | 删除应用
[**app_info**](AppApi.md#app_info) | **GET** /App/{appKey}/Info | 应用详情
[**app_post**](AppApi.md#app_post) | **POST** /App | 创建应用
[**app_put**](AppApi.md#app_put) | **PUT** /App/{appKey} | 更新应用
[**app_transfer**](AppApi.md#app_transfer) | **GET** /App/{appKey}/Transfer | 转移应用
[**apps**](AppApi.md#apps) | **GET** /App | 应用列表


# **app**
> JObjectApiResult app(app_key)

应用详情

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 应用详情
        api_response = api_instance.app(app_key)
        print("The response of AppApi->app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **app2_fa**
> JObjectApiResult app2_fa(app_key)

双因素验证 获取

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 双因素验证 获取
        api_response = api_instance.app2_fa(app_key)
        print("The response of AppApi->app2_fa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app2_fa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **app2_fa_check**
> JObjectApiResult app2_fa_check(app_key, code=code)

双因素验证 验证

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    code = 'code_example' # str |  (optional)

    try:
        # 双因素验证 验证
        api_response = api_instance.app2_fa_check(app_key, code=code)
        print("The response of AppApi->app2_fa_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app2_fa_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
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

# **app_check_version**
> JObjectApiResult app_check_version(app_key, check_only=check_only)

更新应用数据库

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    check_only = True # bool |  (optional) (default to True)

    try:
        # 更新应用数据库
        api_response = api_instance.app_check_version(app_key, check_only=check_only)
        print("The response of AppApi->app_check_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_check_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **check_only** | **bool**|  | [optional] [default to True]

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

# **app_delete**
> JObjectApiResult app_delete(app_key)

删除应用

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 删除应用
        api_response = api_instance.app_delete(app_key)
        print("The response of AppApi->app_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **app_info**
> JObjectApiResult app_info(app_key, prop_code=prop_code)

应用详情

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    prop_code = 'prop_code_example' # str |  (optional)

    try:
        # 应用详情
        api_response = api_instance.app_info(app_key, prop_code=prop_code)
        print("The response of AppApi->app_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **prop_code** | **str**|  | [optional] 

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

# **app_post**
> JObjectApiResult app_post(app=app)

创建应用

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.app import App
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
    api_instance = PMCore.Client.AppApi(api_client)
    app = PMCore.Client.App() # App |  (optional)

    try:
        # 创建应用
        api_response = api_instance.app_post(app=app)
        print("The response of AppApi->app_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | [**App**](App.md)|  | [optional] 

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

# **app_put**
> JObjectApiResult app_put(app_key, app=app)

更新应用

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.app import App
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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    app = PMCore.Client.App() # App |  (optional)

    try:
        # 更新应用
        api_response = api_instance.app_put(app_key, app=app)
        print("The response of AppApi->app_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app** | [**App**](App.md)|  | [optional] 

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

# **app_transfer**
> JObjectApiResult app_transfer(app_key, project_id=project_id)

转移应用

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
    api_instance = PMCore.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    project_id = 56 # int |  (optional)

    try:
        # 转移应用
        api_response = api_instance.app_transfer(app_key, project_id=project_id)
        print("The response of AppApi->app_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **project_id** | **int**|  | [optional] 

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

# **apps**
> JObjectApiResult apps(project_id=project_id, skip=skip, take=take)

应用列表

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
    api_instance = PMCore.Client.AppApi(api_client)
    project_id = 56 # int |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)

    try:
        # 应用列表
        api_response = api_instance.apps(project_id=project_id, skip=skip, take=take)
        print("The response of AppApi->apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 

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

