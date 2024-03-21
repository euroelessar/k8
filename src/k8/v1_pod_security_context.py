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
from .v1_se_linux_options import V1SELinuxOptions
from .v1_seccomp_profile import V1SeccompProfile
from .v1_sysctl import V1Sysctl
from .v1_windows_security_context_options import V1WindowsSecurityContextOptions

class V1PodSecurityContext(BaseModel):
    """
    PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.  # noqa: E501
    """
    fs_group: Optional[StrictInt] = Field(default=None, alias="fsGroup", description="A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.")
    fs_group_change_policy: Optional[StrictStr] = Field(default=None, alias="fsGroupChangePolicy", description="fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are \"OnRootMismatch\" and \"Always\". If not specified, \"Always\" is used. Note that this field cannot be set when spec.os.name is windows.")
    run_as_group: Optional[StrictInt] = Field(default=None, alias="runAsGroup", description="The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.")
    run_as_non_root: Optional[StrictBool] = Field(default=None, alias="runAsNonRoot", description="Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.")
    run_as_user: Optional[StrictInt] = Field(default=None, alias="runAsUser", description="The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.")
    se_linux_options: Optional[V1SELinuxOptions] = Field(default=None, alias="seLinuxOptions")
    seccomp_profile: Optional[V1SeccompProfile] = Field(default=None, alias="seccompProfile")
    supplemental_groups: Optional[conlist(StrictInt)] = Field(default=None, alias="supplementalGroups", description="A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.")
    sysctls: Optional[conlist(V1Sysctl)] = Field(default=None, description="Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.")
    windows_options: Optional[V1WindowsSecurityContextOptions] = Field(default=None, alias="windowsOptions")
    __properties = ["fsGroup", "fsGroupChangePolicy", "runAsGroup", "runAsNonRoot", "runAsUser", "seLinuxOptions", "seccompProfile", "supplementalGroups", "sysctls", "windowsOptions"]

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
    def from_json(cls, json_str: str) -> V1PodSecurityContext:
        """Create an instance of V1PodSecurityContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of se_linux_options
        if self.se_linux_options:
            _dict['seLinuxOptions'] = self.se_linux_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seccomp_profile
        if self.seccomp_profile:
            _dict['seccompProfile'] = self.seccomp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sysctls (list)
        _items = []
        if self.sysctls:
            for _item in self.sysctls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sysctls'] = _items
        # override the default output from pydantic by calling `to_dict()` of windows_options
        if self.windows_options:
            _dict['windowsOptions'] = self.windows_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodSecurityContext:
        """Create an instance of V1PodSecurityContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodSecurityContext.parse_obj(obj)

        _obj = V1PodSecurityContext.parse_obj({
            "fs_group": obj.get("fsGroup"),
            "fs_group_change_policy": obj.get("fsGroupChangePolicy"),
            "run_as_group": obj.get("runAsGroup"),
            "run_as_non_root": obj.get("runAsNonRoot"),
            "run_as_user": obj.get("runAsUser"),
            "se_linux_options": V1SELinuxOptions.from_dict(obj.get("seLinuxOptions")) if obj.get("seLinuxOptions") is not None else None,
            "seccomp_profile": V1SeccompProfile.from_dict(obj.get("seccompProfile")) if obj.get("seccompProfile") is not None else None,
            "supplemental_groups": obj.get("supplementalGroups"),
            "sysctls": [V1Sysctl.from_dict(_item) for _item in obj.get("sysctls")] if obj.get("sysctls") is not None else None,
            "windows_options": V1WindowsSecurityContextOptions.from_dict(obj.get("windowsOptions")) if obj.get("windowsOptions") is not None else None
        })
        return _obj

