# Cloud-agnostic FaaS Wrapper

Wrapper to make functions for simple HTTP request/response functions cloud-agnostic.

Currently supports:

* AWS Lambda
* Azure Functions (v2)
* Google Cloud Functions
* OpenWhisk (used by IBM cloud functions)

For uniformity, this also implements its own `HttpRequest` and `HttpResponse` objects.

The function that is wrapped takes a single argument (of type `HttpRequest`) and should return a single `HttpResponse`.


## Usage

```python
from proxy import proxy

def func(req):
    ...

main = proxy(func)
```
