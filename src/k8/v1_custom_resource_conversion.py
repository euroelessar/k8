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
from .v1_webhook_conversion import V1WebhookConversion

class V1CustomResourceConversion(BaseModel):
    """
    CustomResourceConversion describes how to convert different versions of a CR.  # noqa: E501
    """
    strategy: StrictStr = Field(..., description="strategy specifies how custom resources are converted between versions. Allowed values are: - `\"None\"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `\"Webhook\"`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.")
    webhook: Optional[V1WebhookConversion] = None
    __properties = ["strategy", "webhook"]

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
    def from_json(cls, json_str: str) -> V1CustomResourceConversion:
        """Create an instance of V1CustomResourceConversion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of webhook
        if self.webhook:
            _dict['webhook'] = self.webhook.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomResourceConversion:
        """Create an instance of V1CustomResourceConversion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomResourceConversion.parse_obj(obj)

        _obj = V1CustomResourceConversion.parse_obj({
            "strategy": obj.get("strategy"),
            "webhook": V1WebhookConversion.from_dict(obj.get("webhook")) if obj.get("webhook") is not None else None
        })
        return _obj

