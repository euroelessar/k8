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

class V1VsphereVirtualDiskVolumeSource(BaseModel):
    """
    Represents a vSphere volume resource.  # noqa: E501
    """
    fs_type: Optional[StrictStr] = Field(default=None, alias="fsType", description="fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.")
    storage_policy_id: Optional[StrictStr] = Field(default=None, alias="storagePolicyID", description="storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.")
    storage_policy_name: Optional[StrictStr] = Field(default=None, alias="storagePolicyName", description="storagePolicyName is the storage Policy Based Management (SPBM) profile name.")
    volume_path: StrictStr = Field(..., alias="volumePath", description="volumePath is the path that identifies vSphere volume vmdk")
    __properties = ["fsType", "storagePolicyID", "storagePolicyName", "volumePath"]

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
    def from_json(cls, json_str: str) -> V1VsphereVirtualDiskVolumeSource:
        """Create an instance of V1VsphereVirtualDiskVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1VsphereVirtualDiskVolumeSource:
        """Create an instance of V1VsphereVirtualDiskVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1VsphereVirtualDiskVolumeSource.parse_obj(obj)

        _obj = V1VsphereVirtualDiskVolumeSource.parse_obj({
            "fs_type": obj.get("fsType"),
            "storage_policy_id": obj.get("storagePolicyID"),
            "storage_policy_name": obj.get("storagePolicyName"),
            "volume_path": obj.get("volumePath")
        })
        return _obj


