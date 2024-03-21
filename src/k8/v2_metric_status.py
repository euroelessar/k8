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
from .v2_container_resource_metric_status import V2ContainerResourceMetricStatus
from .v2_external_metric_status import V2ExternalMetricStatus
from .v2_object_metric_status import V2ObjectMetricStatus
from .v2_pods_metric_status import V2PodsMetricStatus
from .v2_resource_metric_status import V2ResourceMetricStatus

class V2MetricStatus(BaseModel):
    """
    MetricStatus describes the last-read state of a single metric.  # noqa: E501
    """
    container_resource: Optional[V2ContainerResourceMetricStatus] = Field(default=None, alias="containerResource")
    external: Optional[V2ExternalMetricStatus] = None
    object: Optional[V2ObjectMetricStatus] = None
    pods: Optional[V2PodsMetricStatus] = None
    resource: Optional[V2ResourceMetricStatus] = None
    type: StrictStr = Field(..., description="type is the type of metric source.  It will be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object. Note: \"ContainerResource\" type is available on when the feature-gate HPAContainerMetrics is enabled")
    __properties = ["containerResource", "external", "object", "pods", "resource", "type"]

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
    def from_json(cls, json_str: str) -> V2MetricStatus:
        """Create an instance of V2MetricStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of container_resource
        if self.container_resource:
            _dict['containerResource'] = self.container_resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external
        if self.external:
            _dict['external'] = self.external.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pods
        if self.pods:
            _dict['pods'] = self.pods.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2MetricStatus:
        """Create an instance of V2MetricStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2MetricStatus.parse_obj(obj)

        _obj = V2MetricStatus.parse_obj({
            "container_resource": V2ContainerResourceMetricStatus.from_dict(obj.get("containerResource")) if obj.get("containerResource") is not None else None,
            "external": V2ExternalMetricStatus.from_dict(obj.get("external")) if obj.get("external") is not None else None,
            "object": V2ObjectMetricStatus.from_dict(obj.get("object")) if obj.get("object") is not None else None,
            "pods": V2PodsMetricStatus.from_dict(obj.get("pods")) if obj.get("pods") is not None else None,
            "resource": V2ResourceMetricStatus.from_dict(obj.get("resource")) if obj.get("resource") is not None else None,
            "type": obj.get("type")
        })
        return _obj

