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

from visier_profile_management_python_sdk.type.accessible_tenant_profile_revoke_request_dto_target_user_ids import AccessibleTenantProfileRevokeRequestDTOTargetUserIds
from visier_profile_management_python_sdk.type.target_tenant_code_dto import TargetTenantCodeDTO

class RequiredAccessibleTenantProfileRevokeRequestDTO(TypedDict):
    pass

class OptionalAccessibleTenantProfileRevokeRequestDTO(TypedDict, total=False):
    targetUserIds: AccessibleTenantProfileRevokeRequestDTOTargetUserIds

    # A list of objects representing the  analytic tenants for removing profiles from each target user ID.
    targetTenantCodes: typing.List[TargetTenantCodeDTO]

class AccessibleTenantProfileRevokeRequestDTO(RequiredAccessibleTenantProfileRevokeRequestDTO, OptionalAccessibleTenantProfileRevokeRequestDTO):
    pass
