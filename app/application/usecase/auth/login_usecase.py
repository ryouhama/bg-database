from dataclasses import dataclass

from app.application.usecase.dto.base import Dto
from app.domain.entity import User
from app.domain.repository_interface.user_repository_interface import \
    UserRepositoryInterface


class LoginUsecaseDto(Dto):
    email: str


class LoginUsecase:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def execute(self, dto: LoginUsecaseDto) -> User:
        user = self.user_repository.find_by_email(dto.email)

        if user:
            return user

        # Userが存在しない場合は、新規作成する
        created_user = self.user_repository.create(email=dto.email)

        return created_user
