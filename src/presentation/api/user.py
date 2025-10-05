from fastapi import APIRouter, HTTPException, Depends
from application.services.user import UserService
from infrastructure.database.mongo import get_database
from infrastructure.repository.user import MongoUserRepository
from domain.models.user import User

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=list[User])
async def list_users(db=Depends(get_database)):
    repo = MongoUserRepository(db)
    service = UserService(repo)
    try:
        users = await service.list_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return users


@user_router.post("/", response_model=User)
async def create_user(user: User, db=Depends(get_database)):
    repo = MongoUserRepository(db)
    service = UserService(repo)
    try:
        created = await service.create_user(user.name, user.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return created


@user_router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db=Depends(get_database)):
    repo = MongoUserRepository(db)
    service = UserService(repo)
    user = await service.find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.delete("/{user_id}")
async def delete_user(user_id: str, db=Depends(get_database)):
    repo = MongoUserRepository(db)
    service = UserService(repo)
    deleted = await service.remove_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "deleted"}
