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

class V1PolicyRule(BaseModel):
    """
    PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.  # noqa: E501
    """
    api_groups: Optional[list[StrictStr]] = Field(default=None, alias="apiGroups", description="APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. \"\" represents the core API group and \"*\" represents all API groups.")
    non_resource_urls: Optional[list[StrictStr]] = Field(default=None, alias="nonResourceURLs", description="NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as \"pods\" or \"secrets\") or non-resource URL paths (such as \"/api\"),  but not both.")
    resource_names: Optional[list[StrictStr]] = Field(default=None, alias="resourceNames", description="ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.")
    resources: Optional[list[StrictStr]] = Field(default=None, description="Resources is a list of resources this rule applies to. '*' represents all resources.")
    verbs: list[StrictStr] = Field(..., description="Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs.")
    __properties = ["apiGroups", "nonResourceURLs", "resourceNames", "resources", "verbs"]

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
    def from_json(cls, json_str: str) -> V1PolicyRule:
        """Create an instance of V1PolicyRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PolicyRule:
        """Create an instance of V1PolicyRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PolicyRule.parse_obj(obj)

        _obj = V1PolicyRule.parse_obj({
            "api_groups": obj.get("apiGroups"),
            "non_resource_urls": obj.get("nonResourceURLs"),
            "resource_names": obj.get("resourceNames"),
            "resources": obj.get("resources"),
            "verbs": obj.get("verbs")
        })
        return _obj


