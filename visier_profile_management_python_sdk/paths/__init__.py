# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_profile_management_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ADMIN_PROFILES = "/v1/admin/profiles"
    V1_ADMIN_PROFILES_ACCESSIBLETENANTS = "/v1/admin/profiles/accessible-tenants"
    V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID = "/v1/admin/profiles/accessible-tenants/{profileId}"
    V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_ASSIGN = "/v1/admin/profiles/accessible-tenants/{profileId}/assign"
    V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_REMOVE = "/v1/admin/profiles/accessible-tenants/{profileId}/remove"
    V1_ADMIN_PROFILES_PROFILE_ID = "/v1/admin/profiles/{profileId}"
    V1_ADMIN_PROFILES_PROFILE_ID_ASSIGN = "/v1/admin/profiles/{profileId}/assign"
    V1_ADMIN_PROFILES_PROFILE_ID_REMOVE = "/v1/admin/profiles/{profileId}/remove"
    V1_ADMIN_USERS_USER_ID_ACCESSIBLETENANTPROFILES = "/v1/admin/users/{userId}/accessible-tenant-profiles"
    V1_ADMIN_USERS_USER_ID_PROFILES = "/v1/admin/users/{userId}/profiles"
