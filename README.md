<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing the profiles assigned to users


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierprofilemanagement.profile_management.assign_analytic_profile`](#visierprofilemanagementprofile_managementassign_analytic_profile)
  * [`visierprofilemanagement.profile_management.assign_profile`](#visierprofilemanagementprofile_managementassign_profile)
  * [`visierprofilemanagement.profile_management.get_all_profiles`](#visierprofilemanagementprofile_managementget_all_profiles)
  * [`visierprofilemanagement.profile_management.get_analytic_profile_detail`](#visierprofilemanagementprofile_managementget_analytic_profile_detail)
  * [`visierprofilemanagement.profile_management.get_analytic_profiles`](#visierprofilemanagementprofile_managementget_analytic_profiles)
  * [`visierprofilemanagement.profile_management.get_analytic_user_profile`](#visierprofilemanagementprofile_managementget_analytic_user_profile)
  * [`visierprofilemanagement.profile_management.get_profile_detail`](#visierprofilemanagementprofile_managementget_profile_detail)
  * [`visierprofilemanagement.profile_management.get_user_profile`](#visierprofilemanagementprofile_managementget_user_profile)
  * [`visierprofilemanagement.profile_management.remove_analytic_profile`](#visierprofilemanagementprofile_managementremove_analytic_profile)
  * [`visierprofilemanagement.profile_management.remove_profile`](#visierprofilemanagementprofile_managementremove_profile)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=ProfileManagement&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_profile_management_python_sdk import VisierProfileManagement, ApiException

visierprofilemanagement = VisierProfileManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Assign an analytic tenant profile to administrating tenant users
    assign_analytic_profile_response = visierprofilemanagement.profile_management.assign_analytic_profile(
        profile_id="profileId_example",
        target_user_ids=[
        "string_example"
    ],
        target_tenant_codes=[
        {
        }
    ],
        validity_start_time="string_example",
        validity_end_time="string_example",
    )
    print(assign_analytic_profile_response)
except ApiException as e:
    print("Exception when calling ProfileManagementApi.assign_analytic_profile: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_profile_management_python_sdk import VisierProfileManagement, ApiException

visierprofilemanagement = VisierProfileManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Assign an analytic tenant profile to administrating tenant users
        assign_analytic_profile_response = await visierprofilemanagement.profile_management.aassign_analytic_profile(
            profile_id="profileId_example",
            target_user_ids=[
        "string_example"
    ],
            target_tenant_codes=[
        {
        }
    ],
            validity_start_time="string_example",
            validity_end_time="string_example",
        )
        print(assign_analytic_profile_response)
    except ApiException as e:
        print("Exception when calling ProfileManagementApi.assign_analytic_profile: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_profile_management_python_sdk import VisierProfileManagement, ApiException

visierprofilemanagement = VisierProfileManagement(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Assign an analytic tenant profile to administrating tenant users
    assign_analytic_profile_response = visierprofilemanagement.profile_management.raw.assign_analytic_profile(
        profile_id="profileId_example",
        target_user_ids=[
        "string_example"
    ],
        target_tenant_codes=[
        {
        }
    ],
        validity_start_time="string_example",
        validity_end_time="string_example",
    )
    pprint(assign_analytic_profile_response.body)
    pprint(assign_analytic_profile_response.body["errors"])
    pprint(assign_analytic_profile_response.body["bad_tenant_codes"])
    pprint(assign_analytic_profile_response.body["bad_user_ids"])
    pprint(assign_analytic_profile_response.body["failed_assignments"])
    pprint(assign_analytic_profile_response.body["successful_assignments"])
    pprint(assign_analytic_profile_response.headers)
    pprint(assign_analytic_profile_response.status)
    pprint(assign_analytic_profile_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ProfileManagementApi.assign_analytic_profile: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierprofilemanagement.profile_management.assign_analytic_profile`<a id="visierprofilemanagementprofile_managementassign_analytic_profile"></a>

This API allows you to assign an analytic tenant profile to a list of administrating tenant users
 for a list of analytic tenants.

 Note:
  - Administrating tenants only.
  - You can revoke a profile from a user with this request by updating the validityEndTime to be
    "less than" the current time (that is, in the past).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_analytic_profile_response = visierprofilemanagement.profile_management.assign_analytic_profile(
    profile_id="profileId_example",
    target_user_ids=[
        "string_example"
    ],
    target_tenant_codes=[
        {
        }
    ],
    validity_start_time="string_example",
    validity_end_time="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to assign.

##### target_user_ids: [`AccessibleTenantProfileAssignmentRequestDTOTargetUserIds`](./visier_profile_management_python_sdk/type/accessible_tenant_profile_assignment_request_dto_target_user_ids.py)<a id="target_user_ids-accessibletenantprofileassignmentrequestdtotargetuseridsvisier_profile_management_python_sdktypeaccessible_tenant_profile_assignment_request_dto_target_user_idspy"></a>

##### target_tenant_codes: List[`TargetTenantCodeDTO`]<a id="target_tenant_codes-listtargettenantcodedto"></a>

A list of objects representing the  analytic tenants for profiles assigned to the users.

##### validity_start_time: `str`<a id="validity_start_time-str"></a>

An inclusive date-time when this profile is active.

##### validity_end_time: `str`<a id="validity_end_time-str"></a>

An exclusive date-time when this profile is no longer active.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessibleTenantProfileAssignmentRequestDTO`](./visier_profile_management_python_sdk/type/accessible_tenant_profile_assignment_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessibleTenantProfileAssignmentResponseDTO`](./visier_profile_management_python_sdk/pydantic/accessible_tenant_profile_assignment_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/accessible-tenants/{profileId}/assign` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.assign_profile`<a id="visierprofilemanagementprofile_managementassign_profile"></a>

This API allows you to assign a profile to a list of users. For administrating tenants,
 this assigns an administrating tenant profile to a list of users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_profile_response = visierprofilemanagement.profile_management.assign_profile(
    profile_id="profileId_example",
    target_user_ids=[
        "string_example"
    ],
    validity_start_time="string_example",
    validity_end_time="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to assign to a list of users.

##### target_user_ids: [`LocalTenantProfileAssignmentRequestDTOTargetUserIds`](./visier_profile_management_python_sdk/type/local_tenant_profile_assignment_request_dto_target_user_ids.py)<a id="target_user_ids-localtenantprofileassignmentrequestdtotargetuseridsvisier_profile_management_python_sdktypelocal_tenant_profile_assignment_request_dto_target_user_idspy"></a>

##### validity_start_time: `str`<a id="validity_start_time-str"></a>

An inclusive date-time when this profile is active.

##### validity_end_time: `str`<a id="validity_end_time-str"></a>

An exclusive date-time when this profile is no longer active.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocalTenantProfileAssignmentRequestDTO`](./visier_profile_management_python_sdk/type/local_tenant_profile_assignment_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LocalTenantProfileAssignmentResponseDTO`](./visier_profile_management_python_sdk/pydantic/local_tenant_profile_assignment_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/{profileId}/assign` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_all_profiles`<a id="visierprofilemanagementprofile_managementget_all_profiles"></a>

This API allows you to get a list of all available profiles. For administrating tenants,
 this retrieves all administrating tenant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_profiles_response = visierprofilemanagement.profile_management.get_all_profiles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfilesGetAPIResponseDTO`](./visier_profile_management_python_sdk/pydantic/profiles_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_analytic_profile_detail`<a id="visierprofilemanagementprofile_managementget_analytic_profile_detail"></a>

This API allows you to get the details of an analytic tenant profile.

 Note: Administrating tenants only.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_analytic_profile_detail_response = visierprofilemanagement.profile_management.get_analytic_profile_detail(
    profile_id="profileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to retrieve details for.

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileGetAPIResponseDTO`](./visier_profile_management_python_sdk/pydantic/profile_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/accessible-tenants/{profileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_analytic_profiles`<a id="visierprofilemanagementprofile_managementget_analytic_profiles"></a>

This API allows you to retrieve a list of profiles available for analytic tenants.

 Note: Administrating tenants only.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_analytic_profiles_response = visierprofilemanagement.profile_management.get_analytic_profiles()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProfilesGetAPIResponseDTO`](./visier_profile_management_python_sdk/pydantic/profiles_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/accessible-tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_analytic_user_profile`<a id="visierprofilemanagementprofile_managementget_analytic_user_profile"></a>

This API allows you to retrieve a specified user's assigned profiles for analytic tenants.

 Note: Administrating tenants only.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_analytic_user_profile_response = visierprofilemanagement.profile_management.get_analytic_user_profile(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`AllProfileAssignedForAccessibleTenantDTO`](./visier_profile_management_python_sdk/pydantic/all_profile_assigned_for_accessible_tenant_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}/accessible-tenant-profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_profile_detail`<a id="visierprofilemanagementprofile_managementget_profile_detail"></a>

This API allows you to get the details of a specific profile. For administrating tenants, this retrieves
 the details of administrating tenant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_profile_detail_response = visierprofilemanagement.profile_management.get_profile_detail(
    profile_id="profileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to retrieve details for.

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileGetAPIResponseDTO`](./visier_profile_management_python_sdk/pydantic/profile_get_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/{profileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.get_user_profile`<a id="visierprofilemanagementprofile_managementget_user_profile"></a>

This API allows you to retrieve a specified user's assigned profiles. For administrating tenants,
 this retrieves a user's administrating tenant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_profile_response = visierprofilemanagement.profile_management.get_user_profile(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`AllProfileAssignedForLocalTenantDTO`](./visier_profile_management_python_sdk/pydantic/all_profile_assigned_for_local_tenant_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/users/{userId}/profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.remove_analytic_profile`<a id="visierprofilemanagementprofile_managementremove_analytic_profile"></a>

This API allows you to remove an analytic tenant profile from a list of administrating tenant users for a list of analytic tenants.

 Note: Administrating tenants only.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_analytic_profile_response = visierprofilemanagement.profile_management.remove_analytic_profile(
    profile_id="profileId_example",
    target_user_ids=[
        "string_example"
    ],
    target_tenant_codes=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to remove.

##### target_user_ids: [`AccessibleTenantProfileRevokeRequestDTOTargetUserIds`](./visier_profile_management_python_sdk/type/accessible_tenant_profile_revoke_request_dto_target_user_ids.py)<a id="target_user_ids-accessibletenantprofilerevokerequestdtotargetuseridsvisier_profile_management_python_sdktypeaccessible_tenant_profile_revoke_request_dto_target_user_idspy"></a>

##### target_tenant_codes: List[`TargetTenantCodeDTO`]<a id="target_tenant_codes-listtargettenantcodedto"></a>

A list of objects representing the  analytic tenants for removing profiles from each target user ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessibleTenantProfileRevokeRequestDTO`](./visier_profile_management_python_sdk/type/accessible_tenant_profile_revoke_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessibleTenantProfileRevokeResponseDTO`](./visier_profile_management_python_sdk/pydantic/accessible_tenant_profile_revoke_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/accessible-tenants/{profileId}/remove` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierprofilemanagement.profile_management.remove_profile`<a id="visierprofilemanagementprofile_managementremove_profile"></a>

This API allows you to remove a profile from a list of users. For administrating tenants, this
 removes an administrating tenant profile from a list of users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_profile_response = visierprofilemanagement.profile_management.remove_profile(
    profile_id="profileId_example",
    target_user_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### profile_id: `str`<a id="profile_id-str"></a>

The ID of the profile to remove to a list of users.

##### target_user_ids: [`LocalTenantProfileRevokeRequestDTOTargetUserIds`](./visier_profile_management_python_sdk/type/local_tenant_profile_revoke_request_dto_target_user_ids.py)<a id="target_user_ids-localtenantprofilerevokerequestdtotargetuseridsvisier_profile_management_python_sdktypelocal_tenant_profile_revoke_request_dto_target_user_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocalTenantProfileRevokeRequestDTO`](./visier_profile_management_python_sdk/type/local_tenant_profile_revoke_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LocalTenantProfileRevokeResponseDTO`](./visier_profile_management_python_sdk/pydantic/local_tenant_profile_revoke_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/profiles/{profileId}/remove` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
