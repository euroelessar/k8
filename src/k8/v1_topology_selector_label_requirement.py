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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist

class V1TopologySelectorLabelRequirement(BaseModel):
    """
    A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.  # noqa: E501
    """
    key: StrictStr = Field(..., description="The label key that the selector applies to.")
    values: conlist(StrictStr) = Field(..., description="An array of string values. One value must match the label to be selected. Each entry in Values is ORed.")
    __properties = ["key", "values"]

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
    def from_json(cls, json_str: str) -> V1TopologySelectorLabelRequirement:
        """Create an instance of V1TopologySelectorLabelRequirement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TopologySelectorLabelRequirement:
        """Create an instance of V1TopologySelectorLabelRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TopologySelectorLabelRequirement.parse_obj(obj)

        _obj = V1TopologySelectorLabelRequirement.parse_obj({
            "key": obj.get("key"),
            "values": obj.get("values")
        })
        return _obj

