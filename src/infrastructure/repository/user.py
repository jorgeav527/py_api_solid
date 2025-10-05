from typing import List, Optional
from bson import ObjectId
from domain.models.user import User
from domain.interfaces.user import UserInterface


class MongoUserRepository(UserInterface):
    """MongoDB implementation of IUserRepository"""

    def __init__(self, db):
        self.collection = db["users"]

    async def get_all(self) -> List[User]:
        users = []
        async for user in self.collection.find():
            users.append(User(**user))
        return users

    async def get_by_id(self, user_id: str) -> Optional[User]:
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        return User(**user) if user else None


    async def create(self, user: User) -> User:
        user_dict = user.model_dump(by_alias=True, exclude_none=True)
        result = await self.collection.insert_one(user_dict)
        user.id = result.inserted_id
        return user

    async def delete(self, user_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count == 1
