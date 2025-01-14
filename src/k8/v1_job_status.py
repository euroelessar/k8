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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods

class V1JobStatus(BaseModel):
    """
    JobStatus represents the current state of a Job.  # noqa: E501
    """
    active: Optional[StrictInt] = Field(default=None, description="The number of pending and running pods.")
    completed_indexes: Optional[StrictStr] = Field(default=None, alias="completedIndexes", description="completedIndexes holds the completed indexes when .spec.completionMode = \"Indexed\" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\".")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime", description="Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully.")
    conditions: Optional[list[V1JobCondition]] = Field(default=None, description="The latest available observations of an object's current state. When a Job fails, one of the conditions will have type \"Failed\" and status true. When a Job is suspended, one of the conditions will have type \"Suspended\" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type \"Complete\" and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/")
    failed: Optional[StrictInt] = Field(default=None, description="The number of pods which reached phase Failed.")
    failed_indexes: Optional[StrictStr] = Field(default=None, alias="failedIndexes", description="FailedIndexes holds the failed indexes when backoffLimitPerIndex=true. The indexes are represented in the text format analogous as for the `completedIndexes` field, ie. they are kept as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the failed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\". This field is beta-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default).")
    ready: Optional[StrictInt] = Field(default=None, description="The number of pods which have a Ready condition.")
    start_time: Optional[datetime] = Field(default=None, alias="startTime", description="Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.")
    succeeded: Optional[StrictInt] = Field(default=None, description="The number of pods which reached phase Succeeded.")
    terminating: Optional[StrictInt] = Field(default=None, description="The number of pods which are terminating (in phase Pending or Running and have a deletionTimestamp).  This field is beta-level. The job controller populates the field when the feature gate JobPodReplacementPolicy is enabled (enabled by default).")
    uncounted_terminated_pods: Optional[V1UncountedTerminatedPods] = Field(default=None, alias="uncountedTerminatedPods")
    __properties = ["active", "completedIndexes", "completionTime", "conditions", "failed", "failedIndexes", "ready", "startTime", "succeeded", "terminating", "uncountedTerminatedPods"]

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
    def from_json(cls, json_str: str) -> V1JobStatus:
        """Create an instance of V1JobStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of uncounted_terminated_pods
        if self.uncounted_terminated_pods:
            _dict['uncountedTerminatedPods'] = self.uncounted_terminated_pods.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1JobStatus:
        """Create an instance of V1JobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1JobStatus.parse_obj(obj)

        _obj = V1JobStatus.parse_obj({
            "active": obj.get("active"),
            "completed_indexes": obj.get("completedIndexes"),
            "completion_time": obj.get("completionTime"),
            "conditions": [V1JobCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "failed": obj.get("failed"),
            "failed_indexes": obj.get("failedIndexes"),
            "ready": obj.get("ready"),
            "start_time": obj.get("startTime"),
            "succeeded": obj.get("succeeded"),
            "terminating": obj.get("terminating"),
            "uncounted_terminated_pods": V1UncountedTerminatedPods.from_dict(obj.get("uncountedTerminatedPods")) if obj.get("uncountedTerminatedPods") is not None else None
        })
        return _obj


