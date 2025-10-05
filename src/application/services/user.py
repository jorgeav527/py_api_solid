from typing import List, Optional
from domain.models.user import User
from infrastructure.repository.user import MongoUserRepository


class UserService:
    """Service layer that applies business logic"""

    def __init__(self, user_repo: MongoUserRepository):
        self.user_repo = user_repo

    async def list_users(self) -> List[User]:
        return await self.user_repo.get_all()

    async def create_user(self, name: str, email: str) -> User:
        # Example of applying a simple business rule
        users = await self.user_repo.get_all()
        if any(u.email == email for u in users):
            raise ValueError("Email already exists")
        user = User(name=name, email=email)
        return await self.user_repo.create(user)

    async def find_user(self, user_id: str) -> Optional[User]:
        return await self.user_repo.get_by_id(user_id)

    async def remove_user(self, user_id: str) -> bool:
        return await self.user_repo.delete(user_id)
