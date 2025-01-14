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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V1LabelSelectorRequirement(BaseModel):
    """
    A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.  # noqa: E501
    """
    key: StrictStr = Field(..., description="key is the label key that the selector applies to.")
    operator: StrictStr = Field(..., description="operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.")
    values: Optional[list[StrictStr]] = Field(default=None, description="values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.")
    __properties = ["key", "operator", "values"]

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
    def from_json(cls, json_str: str) -> V1LabelSelectorRequirement:
        """Create an instance of V1LabelSelectorRequirement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LabelSelectorRequirement:
        """Create an instance of V1LabelSelectorRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LabelSelectorRequirement.parse_obj(obj)

        _obj = V1LabelSelectorRequirement.parse_obj({
            "key": obj.get("key"),
            "operator": obj.get("operator"),
            "values": obj.get("values")
        })
        return _obj


