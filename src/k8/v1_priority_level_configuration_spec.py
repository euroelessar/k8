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
from .v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration
from .v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration

class V1PriorityLevelConfigurationSpec(BaseModel):
    """
    PriorityLevelConfigurationSpec specifies the configuration of a priority level.  # noqa: E501
    """
    exempt: Optional[V1ExemptPriorityLevelConfiguration] = None
    limited: Optional[V1LimitedPriorityLevelConfiguration] = None
    type: StrictStr = Field(..., description="`type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.")
    __properties = ["exempt", "limited", "type"]

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
    def from_json(cls, json_str: str) -> V1PriorityLevelConfigurationSpec:
        """Create an instance of V1PriorityLevelConfigurationSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of exempt
        if self.exempt:
            _dict['exempt'] = self.exempt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limited
        if self.limited:
            _dict['limited'] = self.limited.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PriorityLevelConfigurationSpec:
        """Create an instance of V1PriorityLevelConfigurationSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PriorityLevelConfigurationSpec.parse_obj(obj)

        _obj = V1PriorityLevelConfigurationSpec.parse_obj({
            "exempt": V1ExemptPriorityLevelConfiguration.from_dict(obj.get("exempt")) if obj.get("exempt") is not None else None,
            "limited": V1LimitedPriorityLevelConfiguration.from_dict(obj.get("limited")) if obj.get("limited") is not None else None,
            "type": obj.get("type")
        })
        return _obj


