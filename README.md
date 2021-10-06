# fast-api-opa-demo
Testing various patterns to decouple API application logic from authentication logic

# API Logic
This example assumes an API that exposes a machine learning model and a database with a few simple functionalities:

1. `/predict` - given an input text, predict whether the sentiment is positive, neutral, or negative.
2. `/proprietary` - given an input id, return the labelled input data.
3. `/beta_release_data` - given an input id, return the labelled input data.

# OPA

**Run OPA Unit Tests**

```bash
opa test . -v
```

# Resources
- [opa debugging tips](https://www.openpolicyagent.org/docs/latest/kubernetes-debugging/#check-for-post-requests-in-the-opa-container-logs)
- [opa how base documents work](https://www.openpolicyagent.org/docs/v0.11.0/how-does-opa-work/)
- [opa interactive debugger](https://play.openpolicyagent.org/)
- [opa standalone envoy k8s](https://www.openpolicyagent.org/docs/latest/envoy-tutorial-standalone-envoy/)
- [opa external data](https://www.openpolicyagent.org/docs/latest/external-data/)
- [Medium post with example of envoy/opa pattern](https://medium.com/swlh/securing-dockerized-microservices-with-open-policy-agent-and-envoy-c128dfc764fe)
- [related example of envoy/opa pattern](https://github.com/shanesoh/envoy-opa-compose)
- [opa envoy plugin](https://github.com/open-policy-agent/opa-envoy-plugin#configuration)
- [opa REST API reference (useful for debugging)](https://www.openpolicyagent.org/docs/latest/rest-api/#data-api)
- [opa side of OAuth2 explanation](https://blog.styra.com/blog/integrating-identity-oauth2-and-openid-connect-in-open-policy-agent)
- [identity management system overview](https://curity.io/resources/learn/identity-management-system/)
- * [info: best practices for LDAP/AD and OPA](https://www.openpolicyagent.org/docs/v0.11.0/guides-identity/)
- [JWT explained video](https://www.youtube.com/watch?v=7Q17ubqLfaM)
- [LDAP options](https://en.wikipedia.org/wiki/List_of_LDAP_software)
- [OAuth2.0 short overview video](https://www.youtube.com/watch?v=CPbvxxslDTU)
- [OAuth2.0 and OpenID Connect explanation (long)](https://www.youtube.com/watch?v=996OiexHze0)

## Keycloak
- [Keycloak docs](https://www.keycloak.org/documentation.html)

# Gotchas
- [envoy doesn't process request bodies by default](https://docs.fastly.com/signalsciences/install-guides/envoy/#no-request-bodies-are-processed-by-default)