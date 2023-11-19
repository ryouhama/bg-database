from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entity import User
from app.domain.value_object import UserId


class UserRepositoryInterface(ABC):
    """
    バトルグラウンドに登場するヒーローに関するリポジトリー
    """

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, userId: UserId) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, email: str) -> User:
        raise NotImplementedError()
