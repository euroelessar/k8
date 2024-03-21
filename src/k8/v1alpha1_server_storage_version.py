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

class V1alpha1ServerStorageVersion(BaseModel):
    """
    An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.  # noqa: E501
    """
    api_server_id: Optional[StrictStr] = Field(default=None, alias="apiServerID", description="The ID of the reporting API server.")
    decodable_versions: Optional[conlist(StrictStr)] = Field(default=None, alias="decodableVersions", description="The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.")
    encoding_version: Optional[StrictStr] = Field(default=None, alias="encodingVersion", description="The API server encodes the object to this version when persisting it in the backend (e.g., etcd).")
    served_versions: Optional[conlist(StrictStr)] = Field(default=None, alias="servedVersions", description="The API server can serve these versions. DecodableVersions must include all ServedVersions.")
    __properties = ["apiServerID", "decodableVersions", "encodingVersion", "servedVersions"]

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
    def from_json(cls, json_str: str) -> V1alpha1ServerStorageVersion:
        """Create an instance of V1alpha1ServerStorageVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1alpha1ServerStorageVersion:
        """Create an instance of V1alpha1ServerStorageVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1alpha1ServerStorageVersion.parse_obj(obj)

        _obj = V1alpha1ServerStorageVersion.parse_obj({
            "api_server_id": obj.get("apiServerID"),
            "decodable_versions": obj.get("decodableVersions"),
            "encoding_version": obj.get("encodingVersion"),
            "served_versions": obj.get("servedVersions")
        })
        return _obj

