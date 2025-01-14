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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class V1FCVolumeSource(BaseModel):
    """
    Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.  # noqa: E501
    """
    fs_type: Optional[StrictStr] = Field(default=None, alias="fsType", description="fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.")
    lun: Optional[StrictInt] = Field(default=None, description="lun is Optional: FC target lun number")
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly", description="readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.")
    target_wwns: Optional[list[StrictStr]] = Field(default=None, alias="targetWWNs", description="targetWWNs is Optional: FC target worldwide names (WWNs)")
    wwids: Optional[list[StrictStr]] = Field(default=None, description="wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.")
    __properties = ["fsType", "lun", "readOnly", "targetWWNs", "wwids"]

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
    def from_json(cls, json_str: str) -> V1FCVolumeSource:
        """Create an instance of V1FCVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FCVolumeSource:
        """Create an instance of V1FCVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FCVolumeSource.parse_obj(obj)

        _obj = V1FCVolumeSource.parse_obj({
            "fs_type": obj.get("fsType"),
            "lun": obj.get("lun"),
            "read_only": obj.get("readOnly"),
            "target_wwns": obj.get("targetWWNs"),
            "wwids": obj.get("wwids")
        })
        return _obj


