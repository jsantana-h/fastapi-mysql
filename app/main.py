from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="FastAPI",
    description="A FastAPI example",
    version="0.0.1",
    openapi_tags=[{
        "name": "User",
        "description": "User related operations"
    }],
)
app.include_router(user)


