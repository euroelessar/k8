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
from .v1_label_selector import V1LabelSelector
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from .v1_typed_object_reference import V1TypedObjectReference
from .v1_volume_resource_requirements import V1VolumeResourceRequirements

class V1PersistentVolumeClaimSpec(BaseModel):
    """
    PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes  # noqa: E501
    """
    access_modes: Optional[list[StrictStr]] = Field(default=None, alias="accessModes", description="accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1")
    data_source: Optional[V1TypedLocalObjectReference] = Field(default=None, alias="dataSource")
    data_source_ref: Optional[V1TypedObjectReference] = Field(default=None, alias="dataSourceRef")
    resources: Optional[V1VolumeResourceRequirements] = None
    selector: Optional[V1LabelSelector] = None
    storage_class_name: Optional[StrictStr] = Field(default=None, alias="storageClassName", description="storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1")
    volume_attributes_class_name: Optional[StrictStr] = Field(default=None, alias="volumeAttributesClassName", description="volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#volumeattributesclass (Alpha) Using this field requires the VolumeAttributesClass feature gate to be enabled.")
    volume_mode: Optional[StrictStr] = Field(default=None, alias="volumeMode", description="volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.")
    volume_name: Optional[StrictStr] = Field(default=None, alias="volumeName", description="volumeName is the binding reference to the PersistentVolume backing this claim.")
    __properties = ["accessModes", "dataSource", "dataSourceRef", "resources", "selector", "storageClassName", "volumeAttributesClassName", "volumeMode", "volumeName"]

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
    def from_json(cls, json_str: str) -> V1PersistentVolumeClaimSpec:
        """Create an instance of V1PersistentVolumeClaimSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_source
        if self.data_source:
            _dict['dataSource'] = self.data_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_source_ref
        if self.data_source_ref:
            _dict['dataSourceRef'] = self.data_source_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PersistentVolumeClaimSpec:
        """Create an instance of V1PersistentVolumeClaimSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PersistentVolumeClaimSpec.parse_obj(obj)

        _obj = V1PersistentVolumeClaimSpec.parse_obj({
            "access_modes": obj.get("accessModes"),
            "data_source": V1TypedLocalObjectReference.from_dict(obj.get("dataSource")) if obj.get("dataSource") is not None else None,
            "data_source_ref": V1TypedObjectReference.from_dict(obj.get("dataSourceRef")) if obj.get("dataSourceRef") is not None else None,
            "resources": V1VolumeResourceRequirements.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "selector": V1LabelSelector.from_dict(obj.get("selector")) if obj.get("selector") is not None else None,
            "storage_class_name": obj.get("storageClassName"),
            "volume_attributes_class_name": obj.get("volumeAttributesClassName"),
            "volume_mode": obj.get("volumeMode"),
            "volume_name": obj.get("volumeName")
        })
        return _obj


