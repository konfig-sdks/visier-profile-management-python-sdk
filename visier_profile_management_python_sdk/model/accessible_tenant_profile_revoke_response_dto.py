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


class AccessibleTenantProfileRevokeResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class badTenantCodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReducedTenantCodeErrorDTO']:
                        return ReducedTenantCodeErrorDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ReducedTenantCodeErrorDTO'], typing.List['ReducedTenantCodeErrorDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'badTenantCodes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReducedTenantCodeErrorDTO':
                    return super().__getitem__(i)
            
            
            class badUserIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReducedUserIdErrorDTO']:
                        return ReducedUserIdErrorDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ReducedUserIdErrorDTO'], typing.List['ReducedUserIdErrorDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'badUserIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReducedUserIdErrorDTO':
                    return super().__getitem__(i)
            
            
            class unaffectedUsers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SuccessfulLocalTenantProfileAssignmentDTO']:
                        return SuccessfulLocalTenantProfileAssignmentDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SuccessfulLocalTenantProfileAssignmentDTO'], typing.List['SuccessfulLocalTenantProfileAssignmentDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unaffectedUsers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SuccessfulLocalTenantProfileAssignmentDTO':
                    return super().__getitem__(i)
            
            
            class succeeded(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SuccessfulLocalTenantProfileAssignmentDTO']:
                        return SuccessfulLocalTenantProfileAssignmentDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SuccessfulLocalTenantProfileAssignmentDTO'], typing.List['SuccessfulLocalTenantProfileAssignmentDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'succeeded':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SuccessfulLocalTenantProfileAssignmentDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "badTenantCodes": badTenantCodes,
                "badUserIds": badUserIds,
                "unaffectedUsers": unaffectedUsers,
                "succeeded": succeeded,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badTenantCodes"]) -> MetaOapg.properties.badTenantCodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badUserIds"]) -> MetaOapg.properties.badUserIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unaffectedUsers"]) -> MetaOapg.properties.unaffectedUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["succeeded"]) -> MetaOapg.properties.succeeded: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["badTenantCodes", "badUserIds", "unaffectedUsers", "succeeded", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badTenantCodes"]) -> typing.Union[MetaOapg.properties.badTenantCodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badUserIds"]) -> typing.Union[MetaOapg.properties.badUserIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unaffectedUsers"]) -> typing.Union[MetaOapg.properties.unaffectedUsers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["succeeded"]) -> typing.Union[MetaOapg.properties.succeeded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["badTenantCodes", "badUserIds", "unaffectedUsers", "succeeded", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        badTenantCodes: typing.Union[MetaOapg.properties.badTenantCodes, list, tuple, schemas.Unset] = schemas.unset,
        badUserIds: typing.Union[MetaOapg.properties.badUserIds, list, tuple, schemas.Unset] = schemas.unset,
        unaffectedUsers: typing.Union[MetaOapg.properties.unaffectedUsers, list, tuple, schemas.Unset] = schemas.unset,
        succeeded: typing.Union[MetaOapg.properties.succeeded, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessibleTenantProfileRevokeResponseDTO':
        return super().__new__(
            cls,
            *args,
            badTenantCodes=badTenantCodes,
            badUserIds=badUserIds,
            unaffectedUsers=unaffectedUsers,
            succeeded=succeeded,
            _configuration=_configuration,
            **kwargs,
        )

from visier_profile_management_python_sdk.model.reduced_tenant_code_error_dto import ReducedTenantCodeErrorDTO
from visier_profile_management_python_sdk.model.reduced_user_id_error_dto import ReducedUserIdErrorDTO
from visier_profile_management_python_sdk.model.successful_local_tenant_profile_assignment_dto import SuccessfulLocalTenantProfileAssignmentDTO
