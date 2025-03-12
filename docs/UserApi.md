# PMCore.Client.UserApi

All URIs are relative to *https://api-staging.paomo.fun*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user**](UserApi.md#user) | **GET** /User/{appKey}/{id} | 用户详情
[**user_clear**](UserApi.md#user_clear) | **DELETE** /User/{appKey}/Clear | 清空用户数据
[**user_common_interests**](UserApi.md#user_common_interests) | **GET** /User/{appKey}/Friends/CommonInterests | 有共同爱好的用户推荐
[**user_delete**](UserApi.md#user_delete) | **DELETE** /User/{appKey}/{id} | 删除用户
[**user_email_sign_in**](UserApi.md#user_email_sign_in) | **POST** /User/{appKey}/EmailSignIn | 邮箱登录
[**user_email_sign_up**](UserApi.md#user_email_sign_up) | **POST** /User/{appKey}/EmailSignUp | 邮箱注册
[**user_export**](UserApi.md#user_export) | **GET** /User/{appKey}/Export | 导出用户数据
[**user_follow_user**](UserApi.md#user_follow_user) | **POST** /User/{appKey}/Follower/{userId} | 关注用户
[**user_follower_put**](UserApi.md#user_follower_put) | **PUT** /User/{appKey}/Follower/{id} | 更新粉丝
[**user_followers**](UserApi.md#user_followers) | **GET** /User/{appKey}/Followers | 我的粉丝
[**user_following**](UserApi.md#user_following) | **GET** /User/{appKey}/Following | 我的关注
[**user_friends_near_by**](UserApi.md#user_friends_near_by) | **GET** /User/{appKey}/Friends/NearBy | 附近的用户推荐
[**user_import**](UserApi.md#user_import) | **POST** /User/{appKey}/Import | 导入用户数据
[**user_location**](UserApi.md#user_location) | **GET** /User/{appKey}/Location/{id} | 位置详情
[**user_location_delete**](UserApi.md#user_location_delete) | **DELETE** /User/{appKey}/Location/{id} | 删除位置
[**user_location_post**](UserApi.md#user_location_post) | **POST** /User/{appKey}/Location | 添加位置
[**user_location_put**](UserApi.md#user_location_put) | **PUT** /User/{appKey}/Location/{id} | 更新位置
[**user_locations**](UserApi.md#user_locations) | **GET** /User/{appKey}/Locations | 位置列表
[**user_mutual_followers**](UserApi.md#user_mutual_followers) | **GET** /User/{appKey}/Friends/MutualFollowers | 有共同粉丝的用户推荐
[**user_mutual_followings**](UserApi.md#user_mutual_followings) | **GET** /User/{appKey}/Friends/MutualFollowings | 有共同关注的用户推荐
[**user_o_auth_account_bind**](UserApi.md#user_o_auth_account_bind) | **POST** /User/{appKey}/OAuthAccountBind | 外部账号 绑定
[**user_o_auth_account_sign_in**](UserApi.md#user_o_auth_account_sign_in) | **POST** /User/{appKey}/OAuthAccountSignIn | 外部账号 登录
[**user_o_auth_accounts**](UserApi.md#user_o_auth_accounts) | **GET** /User/{appKey}/OAuthAccounts | 外部账号 绑定列表
[**user_o_auth_accounts_put_bind**](UserApi.md#user_o_auth_accounts_put_bind) | **PUT** /User/{appKey}/OAuthAccounts/{id} | 外部账号 更新绑定
[**user_o_auth_accounts_un_bind**](UserApi.md#user_o_auth_accounts_un_bind) | **DELETE** /User/{appKey}/OAuthAccounts/{id} | 外部账号 删除绑定
[**user_phone_sign_in**](UserApi.md#user_phone_sign_in) | **POST** /User/{appKey}/PhoneSignIn | 手机登录
[**user_phone_sign_up**](UserApi.md#user_phone_sign_up) | **POST** /User/{appKey}/PhoneSignUp | 手机注册
[**user_profile**](UserApi.md#user_profile) | **GET** /User/{appKey}/Profile | 获取个人资料
[**user_put**](UserApi.md#user_put) | **PUT** /User/{appKey}/{id} | 更新用户
[**user_qr_code_pre_sign_in**](UserApi.md#user_qr_code_pre_sign_in) | **POST** /User/{appKey}/QRCodePreSignIn | 微信小程序 - 预登陆
[**user_qr_code_scan**](UserApi.md#user_qr_code_scan) | **POST** /User/{appKey}/QRCodeScan | 微信小程序 - 扫码
[**user_qr_code_sign_in**](UserApi.md#user_qr_code_sign_in) | **POST** /User/{appKey}/QRCodeSignIn | 微信小程序 - 网页登录
[**user_qr_code_sign_up**](UserApi.md#user_qr_code_sign_up) | **POST** /User/{appKey}/QRCodeSignUp | 微信小程序 - 注册
[**user_reset_pwd**](UserApi.md#user_reset_pwd) | **POST** /User/{appKey}/ResetPwd | 重置密码
[**user_send_email_code**](UserApi.md#user_send_email_code) | **POST** /User/{appKey}/SendEmailCode | 发送邮箱验证码
[**user_send_sms_code**](UserApi.md#user_send_sms_code) | **POST** /User/{appKey}/SendSMSCode | 发送手机验证码
[**user_sign_in**](UserApi.md#user_sign_in) | **POST** /User/{appKey}/SignIn | 账号密码 登录
[**user_sign_up**](UserApi.md#user_sign_up) | **POST** /User/{appKey}/SignUp | 账号密码 注册
[**user_two_factor_auth**](UserApi.md#user_two_factor_auth) | **GET** /User/{appKey}/TwoFactorAuth | 双因素验证
[**user_unfollow_user**](UserApi.md#user_unfollow_user) | **DELETE** /User/{appKey}/Follower/{userId} | 取消关注
[**user_union_id_sign_in**](UserApi.md#user_union_id_sign_in) | **POST** /User/{appKey}/UnionIDSignIn | UnionID登录
[**user_union_id_sign_up**](UserApi.md#user_union_id_sign_up) | **POST** /User/{appKey}/UnionIDSignUp | UnionID注册
[**user_update_profile**](UserApi.md#user_update_profile) | **PUT** /User/{appKey}/Profile | 更新个人资料
[**users**](UserApi.md#users) | **GET** /User/{appKey} | 用户列表


# **user**
> JObjectApiResult user(id, app_key)

用户详情

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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 用户详情
        api_response = api_instance.user(id, app_key)
        print("The response of UserApi->user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user: %s\n" % e)
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

# **user_clear**
> JObjectApiResult user_clear(app_key)

清空用户数据

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 清空用户数据
        api_response = api_instance.user_clear(app_key)
        print("The response of UserApi->user_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_clear: %s\n" % e)
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

# **user_common_interests**
> JObjectApiResult user_common_interests(app_key, tag=tag, skip=skip, take=take)

有共同爱好的用户推荐

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 有共同爱好的用户推荐
        api_response = api_instance.user_common_interests(app_key, tag=tag, skip=skip, take=take)
        print("The response of UserApi->user_common_interests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_common_interests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_delete**
> JObjectApiResult user_delete(id, app_key)

删除用户

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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除用户
        api_response = api_instance.user_delete(id, app_key)
        print("The response of UserApi->user_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_delete: %s\n" % e)
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

# **user_email_sign_in**
> JObjectApiResult user_email_sign_in(app_key, email_sign_in_request=email_sign_in_request)

邮箱登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.email_sign_in_request import EmailSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    email_sign_in_request = PMCore.Client.EmailSignInRequest() # EmailSignInRequest |  (optional)

    try:
        # 邮箱登录
        api_response = api_instance.user_email_sign_in(app_key, email_sign_in_request=email_sign_in_request)
        print("The response of UserApi->user_email_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_email_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **email_sign_in_request** | [**EmailSignInRequest**](EmailSignInRequest.md)|  | [optional] 

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

# **user_email_sign_up**
> JObjectApiResult user_email_sign_up(app_key, email_sign_up_request=email_sign_up_request)

邮箱注册

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.email_sign_up_request import EmailSignUpRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    email_sign_up_request = PMCore.Client.EmailSignUpRequest() # EmailSignUpRequest |  (optional)

    try:
        # 邮箱注册
        api_response = api_instance.user_email_sign_up(app_key, email_sign_up_request=email_sign_up_request)
        print("The response of UserApi->user_email_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_email_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **email_sign_up_request** | [**EmailSignUpRequest**](EmailSignUpRequest.md)|  | [optional] 

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

# **user_export**
> bytearray user_export(app_key)

导出用户数据

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 导出用户数据
        api_response = api_instance.user_export(app_key)
        print("The response of UserApi->user_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_follow_user**
> JObjectApiResult user_follow_user(user_id, app_key)

关注用户

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
    api_instance = PMCore.Client.UserApi(api_client)
    user_id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 关注用户
        api_response = api_instance.user_follow_user(user_id, app_key)
        print("The response of UserApi->user_follow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_follow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **user_follower_put**
> JObjectApiResult user_follower_put(id, app_key, follower_put_model=follower_put_model)

更新粉丝

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.follower_put_model import FollowerPutModel
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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    follower_put_model = PMCore.Client.FollowerPutModel() # FollowerPutModel |  (optional)

    try:
        # 更新粉丝
        api_response = api_instance.user_follower_put(id, app_key, follower_put_model=follower_put_model)
        print("The response of UserApi->user_follower_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_follower_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **follower_put_model** | [**FollowerPutModel**](FollowerPutModel.md)|  | [optional] 

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

# **user_followers**
> JObjectApiResult user_followers(app_key, tag=tag, status=status, skip=skip, take=take)

我的粉丝

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 我的粉丝
        api_response = api_instance.user_followers(app_key, tag=tag, status=status, skip=skip, take=take)
        print("The response of UserApi->user_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_following**
> JObjectApiResult user_following(app_key, tag=tag, status=status, skip=skip, take=take)

我的关注

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 我的关注
        api_response = api_instance.user_following(app_key, tag=tag, status=status, skip=skip, take=take)
        print("The response of UserApi->user_following:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_following: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_friends_near_by**
> JObjectApiResult user_friends_near_by(x, y, distance, app_key, gender=gender, age_s=age_s, age_e=age_e, tag=tag, type=type, skip=skip, take=take)

附近的用户推荐

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
    api_instance = PMCore.Client.UserApi(api_client)
    x = 3.4 # float | 纬度
    y = 3.4 # float | 经度
    distance = 56 # int | 附近距离，单位：米
    app_key = 'app_key_example' # str | 
    gender = 'gender_example' # str | 性别 (optional)
    age_s = 56 # int | 年龄段 (optional)
    age_e = 56 # int | 年龄段 (optional)
    tag = 'tag_example' # str | 标签 (optional)
    type = 'type_example' # str | 分类 (optional)
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 附近的用户推荐
        api_response = api_instance.user_friends_near_by(x, y, distance, app_key, gender=gender, age_s=age_s, age_e=age_e, tag=tag, type=type, skip=skip, take=take)
        print("The response of UserApi->user_friends_near_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_friends_near_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **float**| 纬度 | 
 **y** | **float**| 经度 | 
 **distance** | **int**| 附近距离，单位：米 | 
 **app_key** | **str**|  | 
 **gender** | **str**| 性别 | [optional] 
 **age_s** | **int**| 年龄段 | [optional] 
 **age_e** | **int**| 年龄段 | [optional] 
 **tag** | **str**| 标签 | [optional] 
 **type** | **str**| 分类 | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_import**
> JObjectApiResult user_import(app_key, check=check, file=file)

导入用户数据

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    check = True # bool |  (optional)
    file = None # bytearray |  (optional)

    try:
        # 导入用户数据
        api_response = api_instance.user_import(app_key, check=check, file=file)
        print("The response of UserApi->user_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **check** | **bool**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_location**
> JObjectApiResult user_location(id, app_key)

位置详情

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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 位置详情
        api_response = api_instance.user_location(id, app_key)
        print("The response of UserApi->user_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location: %s\n" % e)
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

# **user_location_delete**
> JObjectApiResult user_location_delete(id, app_key)

删除位置

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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除位置
        api_response = api_instance.user_location_delete(id, app_key)
        print("The response of UserApi->user_location_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_delete: %s\n" % e)
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

# **user_location_post**
> JObjectApiResult user_location_post(app_key, geo_location_model=geo_location_model)

添加位置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.geo_location_model import GeoLocationModel
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    geo_location_model = PMCore.Client.GeoLocationModel() # GeoLocationModel |  (optional)

    try:
        # 添加位置
        api_response = api_instance.user_location_post(app_key, geo_location_model=geo_location_model)
        print("The response of UserApi->user_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **geo_location_model** | [**GeoLocationModel**](GeoLocationModel.md)|  | [optional] 

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

# **user_location_put**
> JObjectApiResult user_location_put(id, app_key, geo_location_model=geo_location_model)

更新位置

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.geo_location_model import GeoLocationModel
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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    geo_location_model = PMCore.Client.GeoLocationModel() # GeoLocationModel |  (optional)

    try:
        # 更新位置
        api_response = api_instance.user_location_put(id, app_key, geo_location_model=geo_location_model)
        print("The response of UserApi->user_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **geo_location_model** | [**GeoLocationModel**](GeoLocationModel.md)|  | [optional] 

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

# **user_locations**
> JObjectApiResult user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take)

位置列表

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 标签 (optional)
    type = 'type_example' # str | 分类 (optional)
    x = 3.4 # float | 纬度 (optional)
    y = 3.4 # float | 经度 (optional)
    sphere = 56 # int | 附近距离，单位：米 (optional)
    skip = 56 # int |  (optional)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 位置列表
        api_response = api_instance.user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take)
        print("The response of UserApi->user_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 标签 | [optional] 
 **type** | **str**| 分类 | [optional] 
 **x** | **float**| 纬度 | [optional] 
 **y** | **float**| 经度 | [optional] 
 **sphere** | **int**| 附近距离，单位：米 | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] [default to 10]

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

# **user_mutual_followers**
> JObjectApiResult user_mutual_followers(app_key, skip=skip, take=take)

有共同粉丝的用户推荐

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 有共同粉丝的用户推荐
        api_response = api_instance.user_mutual_followers(app_key, skip=skip, take=take)
        print("The response of UserApi->user_mutual_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_mutual_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_mutual_followings**
> JObjectApiResult user_mutual_followings(app_key, skip=skip, take=take)

有共同关注的用户推荐

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # 有共同关注的用户推荐
        api_response = api_instance.user_mutual_followings(app_key, skip=skip, take=take)
        print("The response of UserApi->user_mutual_followings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_mutual_followings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

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

# **user_o_auth_account_bind**
> JObjectApiResult user_o_auth_account_bind(app_key, o_auth_account_bind_request=o_auth_account_bind_request)

外部账号 绑定

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.o_auth_account_bind_request import OAuthAccountBindRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    o_auth_account_bind_request = PMCore.Client.OAuthAccountBindRequest() # OAuthAccountBindRequest |  (optional)

    try:
        # 外部账号 绑定
        api_response = api_instance.user_o_auth_account_bind(app_key, o_auth_account_bind_request=o_auth_account_bind_request)
        print("The response of UserApi->user_o_auth_account_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_account_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **o_auth_account_bind_request** | [**OAuthAccountBindRequest**](OAuthAccountBindRequest.md)|  | [optional] 

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

# **user_o_auth_account_sign_in**
> JObjectApiResult user_o_auth_account_sign_in(app_key, o_auth_account_sign_in_request=o_auth_account_sign_in_request)

外部账号 登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.o_auth_account_sign_in_request import OAuthAccountSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    o_auth_account_sign_in_request = PMCore.Client.OAuthAccountSignInRequest() # OAuthAccountSignInRequest |  (optional)

    try:
        # 外部账号 登录
        api_response = api_instance.user_o_auth_account_sign_in(app_key, o_auth_account_sign_in_request=o_auth_account_sign_in_request)
        print("The response of UserApi->user_o_auth_account_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_account_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **o_auth_account_sign_in_request** | [**OAuthAccountSignInRequest**](OAuthAccountSignInRequest.md)|  | [optional] 

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

# **user_o_auth_accounts**
> JObjectApiResult user_o_auth_accounts(app_key)

外部账号 绑定列表

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 外部账号 绑定列表
        api_response = api_instance.user_o_auth_accounts(app_key)
        print("The response of UserApi->user_o_auth_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts: %s\n" % e)
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

# **user_o_auth_accounts_put_bind**
> JObjectApiResult user_o_auth_accounts_put_bind(id, app_key, o_auth_account_put_bind_request=o_auth_account_put_bind_request)

外部账号 更新绑定

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.o_auth_account_put_bind_request import OAuthAccountPutBindRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    o_auth_account_put_bind_request = PMCore.Client.OAuthAccountPutBindRequest() # OAuthAccountPutBindRequest |  (optional)

    try:
        # 外部账号 更新绑定
        api_response = api_instance.user_o_auth_accounts_put_bind(id, app_key, o_auth_account_put_bind_request=o_auth_account_put_bind_request)
        print("The response of UserApi->user_o_auth_accounts_put_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts_put_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **o_auth_account_put_bind_request** | [**OAuthAccountPutBindRequest**](OAuthAccountPutBindRequest.md)|  | [optional] 

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

# **user_o_auth_accounts_un_bind**
> JObjectApiResult user_o_auth_accounts_un_bind(id, app_key)

外部账号 删除绑定

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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 外部账号 删除绑定
        api_response = api_instance.user_o_auth_accounts_un_bind(id, app_key)
        print("The response of UserApi->user_o_auth_accounts_un_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts_un_bind: %s\n" % e)
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

# **user_phone_sign_in**
> JObjectApiResult user_phone_sign_in(app_key, phone_sign_in_request=phone_sign_in_request)

手机登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.phone_sign_in_request import PhoneSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    phone_sign_in_request = PMCore.Client.PhoneSignInRequest() # PhoneSignInRequest |  (optional)

    try:
        # 手机登录
        api_response = api_instance.user_phone_sign_in(app_key, phone_sign_in_request=phone_sign_in_request)
        print("The response of UserApi->user_phone_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_phone_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **phone_sign_in_request** | [**PhoneSignInRequest**](PhoneSignInRequest.md)|  | [optional] 

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

# **user_phone_sign_up**
> JObjectApiResult user_phone_sign_up(app_key, phone_sign_up_request=phone_sign_up_request)

手机注册

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.phone_sign_up_request import PhoneSignUpRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    phone_sign_up_request = PMCore.Client.PhoneSignUpRequest() # PhoneSignUpRequest |  (optional)

    try:
        # 手机注册
        api_response = api_instance.user_phone_sign_up(app_key, phone_sign_up_request=phone_sign_up_request)
        print("The response of UserApi->user_phone_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_phone_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **phone_sign_up_request** | [**PhoneSignUpRequest**](PhoneSignUpRequest.md)|  | [optional] 

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

# **user_profile**
> JObjectApiResult user_profile(app_key)

获取个人资料

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 获取个人资料
        api_response = api_instance.user_profile(app_key)
        print("The response of UserApi->user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_profile: %s\n" % e)
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

# **user_put**
> JObjectApiResult user_put(id, app_key, user=user)

更新用户

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.user import User
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
    api_instance = PMCore.Client.UserApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 
    user = PMCore.Client.User() # User |  (optional)

    try:
        # 更新用户
        api_response = api_instance.user_put(id, app_key, user=user)
        print("The response of UserApi->user_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_key** | **str**|  | 
 **user** | [**User**](User.md)|  | [optional] 

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

# **user_qr_code_pre_sign_in**
> JObjectApiResult user_qr_code_pre_sign_in(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)

微信小程序 - 预登陆

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.qr_code_pre_sign_in_request import QRCodePreSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_pre_sign_in_request = PMCore.Client.QRCodePreSignInRequest() # QRCodePreSignInRequest |  (optional)

    try:
        # 微信小程序 - 预登陆
        api_response = api_instance.user_qr_code_pre_sign_in(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)
        print("The response of UserApi->user_qr_code_pre_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_pre_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_pre_sign_in_request** | [**QRCodePreSignInRequest**](QRCodePreSignInRequest.md)|  | [optional] 

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

# **user_qr_code_scan**
> JObjectApiResult user_qr_code_scan(app_key, qr_code_scan_request=qr_code_scan_request)

微信小程序 - 扫码

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.qr_code_scan_request import QRCodeScanRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_scan_request = PMCore.Client.QRCodeScanRequest() # QRCodeScanRequest |  (optional)

    try:
        # 微信小程序 - 扫码
        api_response = api_instance.user_qr_code_scan(app_key, qr_code_scan_request=qr_code_scan_request)
        print("The response of UserApi->user_qr_code_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_scan_request** | [**QRCodeScanRequest**](QRCodeScanRequest.md)|  | [optional] 

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

# **user_qr_code_sign_in**
> JObjectApiResult user_qr_code_sign_in(app_key, qr_code_sign_in_request=qr_code_sign_in_request)

微信小程序 - 网页登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.qr_code_sign_in_request import QRCodeSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_in_request = PMCore.Client.QRCodeSignInRequest() # QRCodeSignInRequest |  (optional)

    try:
        # 微信小程序 - 网页登录
        api_response = api_instance.user_qr_code_sign_in(app_key, qr_code_sign_in_request=qr_code_sign_in_request)
        print("The response of UserApi->user_qr_code_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_in_request** | [**QRCodeSignInRequest**](QRCodeSignInRequest.md)|  | [optional] 

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

# **user_qr_code_sign_up**
> JObjectApiResult user_qr_code_sign_up(app_key, qr_code_sign_up_request=qr_code_sign_up_request)

微信小程序 - 注册

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.qr_code_sign_up_request import QRCodeSignUpRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_up_request = PMCore.Client.QRCodeSignUpRequest() # QRCodeSignUpRequest |  (optional)

    try:
        # 微信小程序 - 注册
        api_response = api_instance.user_qr_code_sign_up(app_key, qr_code_sign_up_request=qr_code_sign_up_request)
        print("The response of UserApi->user_qr_code_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_up_request** | [**QRCodeSignUpRequest**](QRCodeSignUpRequest.md)|  | [optional] 

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

# **user_reset_pwd**
> JObjectApiResult user_reset_pwd(app_key, app_user_reset_pwd_request=app_user_reset_pwd_request)

重置密码

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.app_user_reset_pwd_request import AppUserResetPwdRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    app_user_reset_pwd_request = PMCore.Client.AppUserResetPwdRequest() # AppUserResetPwdRequest |  (optional)

    try:
        # 重置密码
        api_response = api_instance.user_reset_pwd(app_key, app_user_reset_pwd_request=app_user_reset_pwd_request)
        print("The response of UserApi->user_reset_pwd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_reset_pwd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app_user_reset_pwd_request** | [**AppUserResetPwdRequest**](AppUserResetPwdRequest.md)|  | [optional] 

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

# **user_send_email_code**
> JObjectApiResult user_send_email_code(app_key, send_email_code_request=send_email_code_request)

发送邮箱验证码

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.send_email_code_request import SendEmailCodeRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    send_email_code_request = PMCore.Client.SendEmailCodeRequest() # SendEmailCodeRequest |  (optional)

    try:
        # 发送邮箱验证码
        api_response = api_instance.user_send_email_code(app_key, send_email_code_request=send_email_code_request)
        print("The response of UserApi->user_send_email_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_send_email_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **send_email_code_request** | [**SendEmailCodeRequest**](SendEmailCodeRequest.md)|  | [optional] 

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

# **user_send_sms_code**
> JObjectApiResult user_send_sms_code(app_key, send_sms_code_request=send_sms_code_request)

发送手机验证码

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.send_sms_code_request import SendSMSCodeRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    send_sms_code_request = PMCore.Client.SendSMSCodeRequest() # SendSMSCodeRequest |  (optional)

    try:
        # 发送手机验证码
        api_response = api_instance.user_send_sms_code(app_key, send_sms_code_request=send_sms_code_request)
        print("The response of UserApi->user_send_sms_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_send_sms_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **send_sms_code_request** | [**SendSMSCodeRequest**](SendSMSCodeRequest.md)|  | [optional] 

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

# **user_sign_in**
> JObjectApiResult user_sign_in(app_key, sign_in_request=sign_in_request)

账号密码 登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.sign_in_request import SignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_in_request = PMCore.Client.SignInRequest() # SignInRequest |  (optional)

    try:
        # 账号密码 登录
        api_response = api_instance.user_sign_in(app_key, sign_in_request=sign_in_request)
        print("The response of UserApi->user_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **sign_in_request** | [**SignInRequest**](SignInRequest.md)|  | [optional] 

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

# **user_sign_up**
> JObjectApiResult user_sign_up(app_key, sign_up_request=sign_up_request)

账号密码 注册

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.sign_up_request import SignUpRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_up_request = PMCore.Client.SignUpRequest() # SignUpRequest |  (optional)

    try:
        # 账号密码 注册
        api_response = api_instance.user_sign_up(app_key, sign_up_request=sign_up_request)
        print("The response of UserApi->user_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)|  | [optional] 

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

# **user_two_factor_auth**
> JObjectApiResult user_two_factor_auth(app_key)

双因素验证

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 双因素验证
        api_response = api_instance.user_two_factor_auth(app_key)
        print("The response of UserApi->user_two_factor_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_two_factor_auth: %s\n" % e)
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

# **user_unfollow_user**
> JObjectApiResult user_unfollow_user(user_id, app_key)

取消关注

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
    api_instance = PMCore.Client.UserApi(api_client)
    user_id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 取消关注
        api_response = api_instance.user_unfollow_user(user_id, app_key)
        print("The response of UserApi->user_unfollow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_unfollow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
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

# **user_union_id_sign_in**
> JObjectApiResult user_union_id_sign_in(app_key, union_id_sign_in_request=union_id_sign_in_request)

UnionID登录

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.union_id_sign_in_request import UnionIDSignInRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    union_id_sign_in_request = PMCore.Client.UnionIDSignInRequest() # UnionIDSignInRequest |  (optional)

    try:
        # UnionID登录
        api_response = api_instance.user_union_id_sign_in(app_key, union_id_sign_in_request=union_id_sign_in_request)
        print("The response of UserApi->user_union_id_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_union_id_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **union_id_sign_in_request** | [**UnionIDSignInRequest**](UnionIDSignInRequest.md)|  | [optional] 

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

# **user_union_id_sign_up**
> JObjectApiResult user_union_id_sign_up(app_key, union_id_sign_up_request=union_id_sign_up_request)

UnionID注册

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.union_id_sign_up_request import UnionIDSignUpRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    union_id_sign_up_request = PMCore.Client.UnionIDSignUpRequest() # UnionIDSignUpRequest |  (optional)

    try:
        # UnionID注册
        api_response = api_instance.user_union_id_sign_up(app_key, union_id_sign_up_request=union_id_sign_up_request)
        print("The response of UserApi->user_union_id_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_union_id_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **union_id_sign_up_request** | [**UnionIDSignUpRequest**](UnionIDSignUpRequest.md)|  | [optional] 

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

# **user_update_profile**
> JObjectApiResult user_update_profile(app_key, update_profile_request=update_profile_request)

更新个人资料

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.models.update_profile_request import UpdateProfileRequest
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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    update_profile_request = PMCore.Client.UpdateProfileRequest() # UpdateProfileRequest |  (optional)

    try:
        # 更新个人资料
        api_response = api_instance.user_update_profile(app_key, update_profile_request=update_profile_request)
        print("The response of UserApi->user_update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | [optional] 

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

# **users**
> JObjectApiResult users(app_key, user_name=user_name, email=email, phone=phone, platform=platform, union_id=union_id, role=role, skip=skip, take=take)

用户列表

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
    api_instance = PMCore.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    user_name = 'user_name_example' # str |  (optional)
    email = 'email_example' # str |  (optional)
    phone = 'phone_example' # str |  (optional)
    platform = 'platform_example' # str |  (optional)
    union_id = 'union_id_example' # str |  (optional)
    role = 'role_example' # str |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)

    try:
        # 用户列表
        api_response = api_instance.users(app_key, user_name=user_name, email=email, phone=phone, platform=platform, union_id=union_id, role=role, skip=skip, take=take)
        print("The response of UserApi->users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **phone** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **union_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
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

