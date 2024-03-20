import typing_extensions

from visier_profile_management_python_sdk.paths import PathValues
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles import V1AdminProfiles
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_accessible_tenants import V1AdminProfilesAccessibleTenants
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_accessible_tenants_profile_id import V1AdminProfilesAccessibleTenantsProfileId
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_accessible_tenants_profile_id_assign import V1AdminProfilesAccessibleTenantsProfileIdAssign
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_accessible_tenants_profile_id_remove import V1AdminProfilesAccessibleTenantsProfileIdRemove
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_profile_id import V1AdminProfilesProfileId
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_profile_id_assign import V1AdminProfilesProfileIdAssign
from visier_profile_management_python_sdk.apis.paths.v1_admin_profiles_profile_id_remove import V1AdminProfilesProfileIdRemove
from visier_profile_management_python_sdk.apis.paths.v1_admin_users_user_id_accessible_tenant_profiles import V1AdminUsersUserIdAccessibleTenantProfiles
from visier_profile_management_python_sdk.apis.paths.v1_admin_users_user_id_profiles import V1AdminUsersUserIdProfiles

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_PROFILES: V1AdminProfiles,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS: V1AdminProfilesAccessibleTenants,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID: V1AdminProfilesAccessibleTenantsProfileId,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_ASSIGN: V1AdminProfilesAccessibleTenantsProfileIdAssign,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_REMOVE: V1AdminProfilesAccessibleTenantsProfileIdRemove,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID: V1AdminProfilesProfileId,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID_ASSIGN: V1AdminProfilesProfileIdAssign,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID_REMOVE: V1AdminProfilesProfileIdRemove,
        PathValues.V1_ADMIN_USERS_USER_ID_ACCESSIBLETENANTPROFILES: V1AdminUsersUserIdAccessibleTenantProfiles,
        PathValues.V1_ADMIN_USERS_USER_ID_PROFILES: V1AdminUsersUserIdProfiles,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_PROFILES: V1AdminProfiles,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS: V1AdminProfilesAccessibleTenants,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID: V1AdminProfilesAccessibleTenantsProfileId,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_ASSIGN: V1AdminProfilesAccessibleTenantsProfileIdAssign,
        PathValues.V1_ADMIN_PROFILES_ACCESSIBLETENANTS_PROFILE_ID_REMOVE: V1AdminProfilesAccessibleTenantsProfileIdRemove,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID: V1AdminProfilesProfileId,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID_ASSIGN: V1AdminProfilesProfileIdAssign,
        PathValues.V1_ADMIN_PROFILES_PROFILE_ID_REMOVE: V1AdminProfilesProfileIdRemove,
        PathValues.V1_ADMIN_USERS_USER_ID_ACCESSIBLETENANTPROFILES: V1AdminUsersUserIdAccessibleTenantProfiles,
        PathValues.V1_ADMIN_USERS_USER_ID_PROFILES: V1AdminUsersUserIdProfiles,
    }
)
