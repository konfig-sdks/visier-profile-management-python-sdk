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

from visier_profile_management_python_sdk.type.google_protobuf_any import GoogleProtobufAny

class RequiredStatus(TypedDict):
    pass

class OptionalStatus(TypedDict, total=False):
    # The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].
    code: int

    # A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.
    message: str

    # A list of messages that carry the error details.  There is a common set of message types for APIs to use.
    details: typing.List[GoogleProtobufAny]

class Status(RequiredStatus, OptionalStatus):
    pass
