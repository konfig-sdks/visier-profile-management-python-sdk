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

from visier_profile_management_python_sdk.type.failed_local_tenant_profile_revoke_dto import FailedLocalTenantProfileRevokeDTO
from visier_profile_management_python_sdk.type.successful_local_tenant_profile_assignment_dto import SuccessfulLocalTenantProfileAssignmentDTO

class RequiredLocalTenantProfileRevokeResponseDTO(TypedDict):
    pass

class OptionalLocalTenantProfileRevokeResponseDTO(TypedDict, total=False):
    # A list of objects representing any errors that occurred during the assignment operation.
    failed: typing.List[FailedLocalTenantProfileRevokeDTO]

    # A list of the user IDs that successfully had a profile removed.
    succeeded: typing.List[SuccessfulLocalTenantProfileAssignmentDTO]

class LocalTenantProfileRevokeResponseDTO(RequiredLocalTenantProfileRevokeResponseDTO, OptionalLocalTenantProfileRevokeResponseDTO):
    pass
