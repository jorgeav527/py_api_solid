from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.user import User


class UserInterface(ABC):
    """Repository interface for User entity"""

    @abstractmethod
    async def get_all(self) -> List[User]: ...

    @abstractmethod
    async def get_by_id(self, user_id: str) -> Optional[User]: ...

    @abstractmethod
    async def create(self, user: User) -> User: ...

    @abstractmethod
    async def delete(self, user_id: str) -> bool: ...
