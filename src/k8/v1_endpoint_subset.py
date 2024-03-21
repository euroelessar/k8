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
from .core_v1_endpoint_port import CoreV1EndpointPort
from .v1_endpoint_address import V1EndpointAddress

class V1EndpointSubset(BaseModel):
    """
    EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:   {    Addresses: [{\"ip\": \"10.10.1.1\"}, {\"ip\": \"10.10.2.2\"}],    Ports:     [{\"name\": \"a\", \"port\": 8675}, {\"name\": \"b\", \"port\": 309}]  }  The resulting set of endpoints can be viewed as:   a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],  b: [ 10.10.1.1:309, 10.10.2.2:309 ]  # noqa: E501
    """
    addresses: Optional[conlist(V1EndpointAddress)] = Field(default=None, description="IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.")
    not_ready_addresses: Optional[conlist(V1EndpointAddress)] = Field(default=None, alias="notReadyAddresses", description="IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.")
    ports: Optional[conlist(CoreV1EndpointPort)] = Field(default=None, description="Port numbers available on the related IP addresses.")
    __properties = ["addresses", "notReadyAddresses", "ports"]

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
    def from_json(cls, json_str: str) -> V1EndpointSubset:
        """Create an instance of V1EndpointSubset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in not_ready_addresses (list)
        _items = []
        if self.not_ready_addresses:
            for _item in self.not_ready_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notReadyAddresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EndpointSubset:
        """Create an instance of V1EndpointSubset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EndpointSubset.parse_obj(obj)

        _obj = V1EndpointSubset.parse_obj({
            "addresses": [V1EndpointAddress.from_dict(_item) for _item in obj.get("addresses")] if obj.get("addresses") is not None else None,
            "not_ready_addresses": [V1EndpointAddress.from_dict(_item) for _item in obj.get("notReadyAddresses")] if obj.get("notReadyAddresses") is not None else None,
            "ports": [CoreV1EndpointPort.from_dict(_item) for _item in obj.get("ports")] if obj.get("ports") is not None else None
        })
        return _obj

