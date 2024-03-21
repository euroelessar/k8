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

class V1EventSource(BaseModel):
    """
    EventSource contains information for an event.  # noqa: E501
    """
    component: Optional[StrictStr] = Field(default=None, description="Component from which the event is generated.")
    host: Optional[StrictStr] = Field(default=None, description="Node name on which the event is generated.")
    __properties = ["component", "host"]

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
    def from_json(cls, json_str: str) -> V1EventSource:
        """Create an instance of V1EventSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EventSource:
        """Create an instance of V1EventSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EventSource.parse_obj(obj)

        _obj = V1EventSource.parse_obj({
            "component": obj.get("component"),
            "host": obj.get("host")
        })
        return _obj

