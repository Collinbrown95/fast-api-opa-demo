package envoy.authz

import input.attributes.request.http as http_request

# By default, do not allow
default allow = false

# Allow the action if the user is granted permission to perform the action
allow {
    # See if a grant can be found for the requesting user
    some grant
    user_is_granted[grant]
    # Check if the grant permits the action/type for the requesting user
    http_request.method == grant.action
    # Check if any element of the parsed path contains the grant type
    some i
    input.parsed_path[i] == grant.type
}

user_is_granted[grant] {
    some i, j
    # `role` can be assigned an element of the user_roles of this user
    role := data.user_roles[input.parsed_body.user][i]
    # `grant` can be assigned a single grant from the role_grants for the selected `role`
    grant := data.role_grants[role][j]
}