from fastapi import FastAPI
from contextlib import asynccontextmanager
from presentation.api.user import user_router
from infrastructure.database.mongo import connect_to_mongo, close_mongo_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(
    title="User Clean Architecture API",
    lifespan=lifespan,
)

# Include router
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Clean Architecture API!"}
