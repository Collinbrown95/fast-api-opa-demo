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