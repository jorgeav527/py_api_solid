from fastapi import FastAPI
from presentation.api.user import user_router

app = FastAPI(title="User Clean Architecture API")

# Include router
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Clean Architecture API!"}
