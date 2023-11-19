from typing import Optional

from app.domain.entity import User
from app.domain.repository_interface.user_repository_interface import \
    UserRepositoryInterface
from app.domain.value_object import UserId
from app.infrastructure.db import get_client


class UserRepository(UserRepositoryInterface):
    client = get_client()

    def find_by_jwt(self, jwt: str) -> Optional[User]:
        res = self.client.auth.get_user(jwt)

        if res is None:
            return None

        return User(
            id=UserId.generate(res.user.id),
        )

    def create(self, email: str, password: str) -> User:
        res = self.client.auth.sign_up({"email": email, "password": password})

        return User(
            id=UserId.generate(res.user.id),
        )

    def exist(self, email: str) -> bool:
        ...
