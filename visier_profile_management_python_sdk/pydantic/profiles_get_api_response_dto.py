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

from visier_profile_management_python_sdk.pydantic.profile_get_api_response_dto import ProfileGetAPIResponseDTO

class ProfilesGetAPIResponseDTO(BaseModel):
    # A list of objects representing the available profiles.
    profiles: typing.Optional[typing.List[ProfileGetAPIResponseDTO]] = Field(None, alias='profiles')
    class Config:
        arbitrary_types_allowed = True
