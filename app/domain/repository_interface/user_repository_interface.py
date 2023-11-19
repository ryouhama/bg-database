from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entity import User


class UserRepositoryInterface(ABC):
    """
    バトルグラウンドに登場するヒーローに関するリポジトリー
    """

    @abstractmethod
    def find_by_jwt(self, jwt: str) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, email: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    def exist(self, email: str) -> bool:
        raise NotImplementedError()
