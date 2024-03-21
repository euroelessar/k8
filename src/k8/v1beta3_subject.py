# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from .v1beta3_group_subject import V1beta3GroupSubject
from .v1beta3_service_account_subject import V1beta3ServiceAccountSubject
from .v1beta3_user_subject import V1beta3UserSubject

class V1beta3Subject(BaseModel):
    """
    Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.  # noqa: E501
    """
    group: Optional[V1beta3GroupSubject] = None
    kind: StrictStr = Field(..., description="`kind` indicates which one of the other fields is non-empty. Required")
    service_account: Optional[V1beta3ServiceAccountSubject] = Field(default=None, alias="serviceAccount")
    user: Optional[V1beta3UserSubject] = None
    __properties = ["group", "kind", "serviceAccount", "user"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1beta3Subject:
        """Create an instance of V1beta3Subject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account
        if self.service_account:
            _dict['serviceAccount'] = self.service_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta3Subject:
        """Create an instance of V1beta3Subject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta3Subject.parse_obj(obj)

        _obj = V1beta3Subject.parse_obj({
            "group": V1beta3GroupSubject.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "kind": obj.get("kind"),
            "service_account": V1beta3ServiceAccountSubject.from_dict(obj.get("serviceAccount")) if obj.get("serviceAccount") is not None else None,
            "user": V1beta3UserSubject.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj

