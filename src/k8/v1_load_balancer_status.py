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
from pydantic import BaseModel, Field, conlist
from .v1_load_balancer_ingress import V1LoadBalancerIngress

class V1LoadBalancerStatus(BaseModel):
    """
    LoadBalancerStatus represents the status of a load-balancer.  # noqa: E501
    """
    ingress: Optional[list[V1LoadBalancerIngress]] = Field(default=None, description="Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.")
    __properties = ["ingress"]

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
    def from_json(cls, json_str: str) -> V1LoadBalancerStatus:
        """Create an instance of V1LoadBalancerStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ingress (list)
        _items = []
        if self.ingress:
            for _item in self.ingress:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ingress'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LoadBalancerStatus:
        """Create an instance of V1LoadBalancerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LoadBalancerStatus.parse_obj(obj)

        _obj = V1LoadBalancerStatus.parse_obj({
            "ingress": [V1LoadBalancerIngress.from_dict(_item) for _item in obj.get("ingress")] if obj.get("ingress") is not None else None
        })
        return _obj


