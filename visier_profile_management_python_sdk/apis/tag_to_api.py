import typing_extensions

from visier_profile_management_python_sdk.apis.tags import TagValues
from visier_profile_management_python_sdk.apis.tags.profile_management_api import ProfileManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROFILE_MANAGEMENT: ProfileManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROFILE_MANAGEMENT: ProfileManagementApi,
    }
)
