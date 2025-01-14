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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from .v1_bound_object_reference import V1BoundObjectReference

class V1TokenRequestSpec(BaseModel):
    """
    TokenRequestSpec contains client provided parameters of a token request.  # noqa: E501
    """
    audiences: list[StrictStr] = Field(..., description="Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.")
    bound_object_ref: Optional[V1BoundObjectReference] = Field(default=None, alias="boundObjectRef")
    expiration_seconds: Optional[StrictInt] = Field(default=None, alias="expirationSeconds", description="ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.")
    __properties = ["audiences", "boundObjectRef", "expirationSeconds"]

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
    def from_json(cls, json_str: str) -> V1TokenRequestSpec:
        """Create an instance of V1TokenRequestSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bound_object_ref
        if self.bound_object_ref:
            _dict['boundObjectRef'] = self.bound_object_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TokenRequestSpec:
        """Create an instance of V1TokenRequestSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TokenRequestSpec.parse_obj(obj)

        _obj = V1TokenRequestSpec.parse_obj({
            "audiences": obj.get("audiences"),
            "bound_object_ref": V1BoundObjectReference.from_dict(obj.get("boundObjectRef")) if obj.get("boundObjectRef") is not None else None,
            "expiration_seconds": obj.get("expirationSeconds")
        })
        return _obj


