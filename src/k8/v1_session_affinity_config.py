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
from pydantic import BaseModel, Field
from .v1_client_ip_config import V1ClientIPConfig

class V1SessionAffinityConfig(BaseModel):
    """
    SessionAffinityConfig represents the configurations of session affinity.  # noqa: E501
    """
    client_ip: Optional[V1ClientIPConfig] = Field(default=None, alias="clientIP")
    __properties = ["clientIP"]

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
    def from_json(cls, json_str: str) -> V1SessionAffinityConfig:
        """Create an instance of V1SessionAffinityConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of client_ip
        if self.client_ip:
            _dict['clientIP'] = self.client_ip.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SessionAffinityConfig:
        """Create an instance of V1SessionAffinityConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SessionAffinityConfig.parse_obj(obj)

        _obj = V1SessionAffinityConfig.parse_obj({
            "client_ip": V1ClientIPConfig.from_dict(obj.get("clientIP")) if obj.get("clientIP") is not None else None
        })
        return _obj


