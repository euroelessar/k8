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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class V1Taint(BaseModel):
    """
    The node this Taint is attached to has the \"effect\" on any pod that does not tolerate the Taint.  # noqa: E501
    """
    effect: StrictStr = Field(..., description="Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.")
    key: StrictStr = Field(..., description="Required. The taint key to be applied to a node.")
    time_added: Optional[datetime] = Field(default=None, alias="timeAdded", description="TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.")
    value: Optional[StrictStr] = Field(default=None, description="The taint value corresponding to the taint key.")
    __properties = ["effect", "key", "timeAdded", "value"]

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
    def from_json(cls, json_str: str) -> V1Taint:
        """Create an instance of V1Taint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Taint:
        """Create an instance of V1Taint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Taint.parse_obj(obj)

        _obj = V1Taint.parse_obj({
            "effect": obj.get("effect"),
            "key": obj.get("key"),
            "time_added": obj.get("timeAdded"),
            "value": obj.get("value")
        })
        return _obj


