# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_profile_management_python_sdk import schemas  # noqa: F401


class AccessibleTenantProfileAssignmentRequestDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def targetUserIds() -> typing.Type['AccessibleTenantProfileAssignmentRequestDTOTargetUserIds']:
                return AccessibleTenantProfileAssignmentRequestDTOTargetUserIds
            
            
            class targetTenantCodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TargetTenantCodeDTO']:
                        return TargetTenantCodeDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TargetTenantCodeDTO'], typing.List['TargetTenantCodeDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetTenantCodes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TargetTenantCodeDTO':
                    return super().__getitem__(i)
            validityStartTime = schemas.StrSchema
            validityEndTime = schemas.StrSchema
            __annotations__ = {
                "targetUserIds": targetUserIds,
                "targetTenantCodes": targetTenantCodes,
                "validityStartTime": validityStartTime,
                "validityEndTime": validityEndTime,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetUserIds"]) -> 'AccessibleTenantProfileAssignmentRequestDTOTargetUserIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetTenantCodes"]) -> MetaOapg.properties.targetTenantCodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validityStartTime"]) -> MetaOapg.properties.validityStartTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validityEndTime"]) -> MetaOapg.properties.validityEndTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["targetUserIds", "targetTenantCodes", "validityStartTime", "validityEndTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetUserIds"]) -> typing.Union['AccessibleTenantProfileAssignmentRequestDTOTargetUserIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetTenantCodes"]) -> typing.Union[MetaOapg.properties.targetTenantCodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validityStartTime"]) -> typing.Union[MetaOapg.properties.validityStartTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validityEndTime"]) -> typing.Union[MetaOapg.properties.validityEndTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["targetUserIds", "targetTenantCodes", "validityStartTime", "validityEndTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        targetUserIds: typing.Union['AccessibleTenantProfileAssignmentRequestDTOTargetUserIds', schemas.Unset] = schemas.unset,
        targetTenantCodes: typing.Union[MetaOapg.properties.targetTenantCodes, list, tuple, schemas.Unset] = schemas.unset,
        validityStartTime: typing.Union[MetaOapg.properties.validityStartTime, str, schemas.Unset] = schemas.unset,
        validityEndTime: typing.Union[MetaOapg.properties.validityEndTime, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessibleTenantProfileAssignmentRequestDTO':
        return super().__new__(
            cls,
            *args,
            targetUserIds=targetUserIds,
            targetTenantCodes=targetTenantCodes,
            validityStartTime=validityStartTime,
            validityEndTime=validityEndTime,
            _configuration=_configuration,
            **kwargs,
        )

from visier_profile_management_python_sdk.model.accessible_tenant_profile_assignment_request_dto_target_user_ids import AccessibleTenantProfileAssignmentRequestDTOTargetUserIds
from visier_profile_management_python_sdk.model.target_tenant_code_dto import TargetTenantCodeDTO
