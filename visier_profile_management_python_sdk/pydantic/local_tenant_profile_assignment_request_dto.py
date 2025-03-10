# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from visier_profile_management_python_sdk.pydantic.local_tenant_profile_assignment_request_dto_target_user_ids import LocalTenantProfileAssignmentRequestDTOTargetUserIds

class LocalTenantProfileAssignmentRequestDTO(BaseModel):
    target_user_ids: typing.Optional[LocalTenantProfileAssignmentRequestDTOTargetUserIds] = Field(None, alias='targetUserIds')

    # An inclusive date-time when this profile is active.
    validity_start_time: typing.Optional[str] = Field(None, alias='validityStartTime')

    # An exclusive date-time when this profile is no longer active.
    validity_end_time: typing.Optional[str] = Field(None, alias='validityEndTime')
    class Config:
        arbitrary_types_allowed = True
