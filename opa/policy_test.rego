package envoy.authz

test_post_proprietary_allowed {
    allow with input as {"user": "alice", "action": "POST", "type": "proprietary"}
}

test_post_proprietary_not_allowed {
    not allow with input as {"user": "bob", "action": "POST", "type": "proprietary"}
}