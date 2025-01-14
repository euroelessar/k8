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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from .v1_scope_selector import V1ScopeSelector

class V1ResourceQuotaSpec(BaseModel):
    """
    ResourceQuotaSpec defines the desired hard limits to enforce for Quota.  # noqa: E501
    """
    hard: Optional[Dict[str, StrictStr]] = Field(default=None, description="hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/")
    scope_selector: Optional[V1ScopeSelector] = Field(default=None, alias="scopeSelector")
    scopes: Optional[list[StrictStr]] = Field(default=None, description="A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.")
    __properties = ["hard", "scopeSelector", "scopes"]

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
    def from_json(cls, json_str: str) -> V1ResourceQuotaSpec:
        """Create an instance of V1ResourceQuotaSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of scope_selector
        if self.scope_selector:
            _dict['scopeSelector'] = self.scope_selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ResourceQuotaSpec:
        """Create an instance of V1ResourceQuotaSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ResourceQuotaSpec.parse_obj(obj)

        _obj = V1ResourceQuotaSpec.parse_obj({
            "hard": obj.get("hard"),
            "scope_selector": V1ScopeSelector.from_dict(obj.get("scopeSelector")) if obj.get("scopeSelector") is not None else None,
            "scopes": obj.get("scopes")
        })
        return _obj


