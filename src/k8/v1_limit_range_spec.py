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
from pydantic import BaseModel, Field, conlist
from .v1_limit_range_item import V1LimitRangeItem

class V1LimitRangeSpec(BaseModel):
    """
    LimitRangeSpec defines a min/max usage limit for resources that match on kind.  # noqa: E501
    """
    limits: conlist(V1LimitRangeItem) = Field(..., description="Limits is the list of LimitRangeItem objects that are enforced.")
    __properties = ["limits"]

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
    def from_json(cls, json_str: str) -> V1LimitRangeSpec:
        """Create an instance of V1LimitRangeSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in limits (list)
        _items = []
        if self.limits:
            for _item in self.limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['limits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LimitRangeSpec:
        """Create an instance of V1LimitRangeSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LimitRangeSpec.parse_obj(obj)

        _obj = V1LimitRangeSpec.parse_obj({
            "limits": [V1LimitRangeItem.from_dict(_item) for _item in obj.get("limits")] if obj.get("limits") is not None else None
        })
        return _obj

