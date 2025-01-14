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



from pydantic import BaseModel, Field, StrictStr

class V1NodeSystemInfo(BaseModel):
    """
    NodeSystemInfo is a set of ids/uuids to uniquely identify the node.  # noqa: E501
    """
    architecture: StrictStr = Field(..., description="The Architecture reported by the node")
    boot_id: StrictStr = Field(..., alias="bootID", description="Boot ID reported by the node.")
    container_runtime_version: StrictStr = Field(..., alias="containerRuntimeVersion", description="ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).")
    kernel_version: StrictStr = Field(..., alias="kernelVersion", description="Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).")
    kube_proxy_version: StrictStr = Field(..., alias="kubeProxyVersion", description="KubeProxy Version reported by the node.")
    kubelet_version: StrictStr = Field(..., alias="kubeletVersion", description="Kubelet Version reported by the node.")
    machine_id: StrictStr = Field(..., alias="machineID", description="MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html")
    operating_system: StrictStr = Field(..., alias="operatingSystem", description="The Operating System reported by the node")
    os_image: StrictStr = Field(..., alias="osImage", description="OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).")
    system_uuid: StrictStr = Field(..., alias="systemUUID", description="SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid")
    __properties = ["architecture", "bootID", "containerRuntimeVersion", "kernelVersion", "kubeProxyVersion", "kubeletVersion", "machineID", "operatingSystem", "osImage", "systemUUID"]

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
    def from_json(cls, json_str: str) -> V1NodeSystemInfo:
        """Create an instance of V1NodeSystemInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NodeSystemInfo:
        """Create an instance of V1NodeSystemInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NodeSystemInfo.parse_obj(obj)

        _obj = V1NodeSystemInfo.parse_obj({
            "architecture": obj.get("architecture"),
            "boot_id": obj.get("bootID"),
            "container_runtime_version": obj.get("containerRuntimeVersion"),
            "kernel_version": obj.get("kernelVersion"),
            "kube_proxy_version": obj.get("kubeProxyVersion"),
            "kubelet_version": obj.get("kubeletVersion"),
            "machine_id": obj.get("machineID"),
            "operating_system": obj.get("operatingSystem"),
            "os_image": obj.get("osImage"),
            "system_uuid": obj.get("systemUUID")
        })
        return _obj


