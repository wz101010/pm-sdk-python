# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: Optional[StrictInt] = None
    platform: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    union_id: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="unionID")
    nick_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, alias="nickName")
    avatar: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    data: Optional[StrictStr] = None
    user_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, alias="userName")
    pwd: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    email: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    email_is_valid: Optional[StrictBool] = Field(default=None, alias="emailIsValid")
    phone: Optional[Annotated[str, Field(strict=True, max_length=20)]] = None
    phone_is_valid: Optional[StrictBool] = Field(default=None, alias="phoneIsValid")
    relation_chain: Optional[StrictStr] = Field(default=None, alias="relationChain")
    interest_tags: Optional[StrictStr] = Field(default=None, alias="interestTags")
    biography: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    gender: Optional[Annotated[str, Field(strict=True, max_length=15)]] = None
    birthday: Optional[datetime] = None
    occupation: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    education: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    contact: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    languages: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    social_links: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="socialLinks")
    relationship_status: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, alias="relationshipStatus")
    company: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    industry: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    company_position: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, alias="companyPosition")
    private_settings: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="privateSettings")
    is_lock: Optional[StrictBool] = Field(default=None, alias="isLock")
    lock_until: Optional[datetime] = Field(default=None, alias="lockUntil")
    enable_user_name_sign_in: Optional[StrictBool] = Field(default=None, alias="enableUserNameSignIn")
    enable_email_sign_in: Optional[StrictBool] = Field(default=None, alias="enableEmailSignIn")
    enable_phone_sign_in: Optional[StrictBool] = Field(default=None, alias="enablePhoneSignIn")
    enable_union_id_sign_in: Optional[StrictBool] = Field(default=None, alias="enableUnionIDSignIn")
    enable_o_auth: Optional[StrictBool] = Field(default=None, alias="enableOAuth")
    enable2_fa_auth: Optional[StrictBool] = Field(default=None, alias="enable2FAAuth")
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    __properties: ClassVar[List[str]] = ["id", "platform", "unionID", "nickName", "avatar", "data", "userName", "pwd", "email", "emailIsValid", "phone", "phoneIsValid", "relationChain", "interestTags", "biography", "gender", "birthday", "occupation", "education", "contact", "languages", "socialLinks", "relationshipStatus", "company", "industry", "companyPosition", "privateSettings", "isLock", "lockUntil", "enableUserNameSignIn", "enableEmailSignIn", "enablePhoneSignIn", "enableUnionIDSignIn", "enableOAuth", "enable2FAAuth", "createDate", "lastUpdate"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if union_id (nullable) is None
        # and model_fields_set contains the field
        if self.union_id is None and "union_id" in self.model_fields_set:
            _dict['unionID'] = None

        # set to None if nick_name (nullable) is None
        # and model_fields_set contains the field
        if self.nick_name is None and "nick_name" in self.model_fields_set:
            _dict['nickName'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if pwd (nullable) is None
        # and model_fields_set contains the field
        if self.pwd is None and "pwd" in self.model_fields_set:
            _dict['pwd'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if relation_chain (nullable) is None
        # and model_fields_set contains the field
        if self.relation_chain is None and "relation_chain" in self.model_fields_set:
            _dict['relationChain'] = None

        # set to None if interest_tags (nullable) is None
        # and model_fields_set contains the field
        if self.interest_tags is None and "interest_tags" in self.model_fields_set:
            _dict['interestTags'] = None

        # set to None if biography (nullable) is None
        # and model_fields_set contains the field
        if self.biography is None and "biography" in self.model_fields_set:
            _dict['biography'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if occupation (nullable) is None
        # and model_fields_set contains the field
        if self.occupation is None and "occupation" in self.model_fields_set:
            _dict['occupation'] = None

        # set to None if education (nullable) is None
        # and model_fields_set contains the field
        if self.education is None and "education" in self.model_fields_set:
            _dict['education'] = None

        # set to None if contact (nullable) is None
        # and model_fields_set contains the field
        if self.contact is None and "contact" in self.model_fields_set:
            _dict['contact'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if social_links (nullable) is None
        # and model_fields_set contains the field
        if self.social_links is None and "social_links" in self.model_fields_set:
            _dict['socialLinks'] = None

        # set to None if relationship_status (nullable) is None
        # and model_fields_set contains the field
        if self.relationship_status is None and "relationship_status" in self.model_fields_set:
            _dict['relationshipStatus'] = None

        # set to None if company (nullable) is None
        # and model_fields_set contains the field
        if self.company is None and "company" in self.model_fields_set:
            _dict['company'] = None

        # set to None if industry (nullable) is None
        # and model_fields_set contains the field
        if self.industry is None and "industry" in self.model_fields_set:
            _dict['industry'] = None

        # set to None if company_position (nullable) is None
        # and model_fields_set contains the field
        if self.company_position is None and "company_position" in self.model_fields_set:
            _dict['companyPosition'] = None

        # set to None if private_settings (nullable) is None
        # and model_fields_set contains the field
        if self.private_settings is None and "private_settings" in self.model_fields_set:
            _dict['privateSettings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "platform": obj.get("platform"),
            "unionID": obj.get("unionID"),
            "nickName": obj.get("nickName"),
            "avatar": obj.get("avatar"),
            "data": obj.get("data"),
            "userName": obj.get("userName"),
            "pwd": obj.get("pwd"),
            "email": obj.get("email"),
            "emailIsValid": obj.get("emailIsValid"),
            "phone": obj.get("phone"),
            "phoneIsValid": obj.get("phoneIsValid"),
            "relationChain": obj.get("relationChain"),
            "interestTags": obj.get("interestTags"),
            "biography": obj.get("biography"),
            "gender": obj.get("gender"),
            "birthday": obj.get("birthday"),
            "occupation": obj.get("occupation"),
            "education": obj.get("education"),
            "contact": obj.get("contact"),
            "languages": obj.get("languages"),
            "socialLinks": obj.get("socialLinks"),
            "relationshipStatus": obj.get("relationshipStatus"),
            "company": obj.get("company"),
            "industry": obj.get("industry"),
            "companyPosition": obj.get("companyPosition"),
            "privateSettings": obj.get("privateSettings"),
            "isLock": obj.get("isLock"),
            "lockUntil": obj.get("lockUntil"),
            "enableUserNameSignIn": obj.get("enableUserNameSignIn"),
            "enableEmailSignIn": obj.get("enableEmailSignIn"),
            "enablePhoneSignIn": obj.get("enablePhoneSignIn"),
            "enableUnionIDSignIn": obj.get("enableUnionIDSignIn"),
            "enableOAuth": obj.get("enableOAuth"),
            "enable2FAAuth": obj.get("enable2FAAuth"),
            "createDate": obj.get("createDate"),
            "lastUpdate": obj.get("lastUpdate")
        })
        return _obj


