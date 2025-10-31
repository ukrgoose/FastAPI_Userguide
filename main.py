from fastapi import FastAPI
from . import (
    first_steps, path_params, query_params, request_body,
    query_string_validations, path_numeric_validations, query_param_models,
    body_multiple_params, body_fields, body_nested_models,
    request_examples, extra_types
)

app = FastAPI(title="FastAPI User Guide Examples")

app.include_router(first_steps.router, prefix="/first-steps", tags=["First Steps"])
app.include_router(path_params.router, prefix="/path-params", tags=["Path Parameters"])
app.include_router(query_params.router, prefix="/query-params", tags=["Query Parameters"])
app.include_router(request_body.router, prefix="/request-body", tags=["Request Body"])
app.include_router(query_string_validations.router, prefix="/query-validate", tags=["Query Validations"])
app.include_router(path_numeric_validations.router, prefix="/path-validate", tags=["Path Numeric Validations"])
app.include_router(query_param_models.router, prefix="/query-models", tags=["Query Param Models"])
app.include_router(body_multiple_params.router, prefix="/body-multi", tags=["Body - Multiple Params"])
app.include_router(body_fields.router, prefix="/body-fields", tags=["Body - Fields"])
app.include_router(body_nested_models.router, prefix="/body-nested", tags=["Body - Nested Models"])
app.include_router(request_examples.router, prefix="/request-examples", tags=["Request Example Data"])
app.include_router(extra_types.router, prefix="/extra-types", tags=["Extra Data Types"])

@app.get("/", tags=["Root"])
def root():
    return {"ok": True, "message": "See /docs for endpoints"}
