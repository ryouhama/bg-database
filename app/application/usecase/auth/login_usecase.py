from app.application.exception import ApplicationException
from app.application.usecase.dto.base import Dto, MaskedString
from app.domain.entity import User
from app.domain.repository_interface import UserRepositoryInterface


class LoginUsecaseDto(Dto):
    email: str
    password: MaskedString


class LoginUsecase:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def execute(self, dto: LoginUsecaseDto) -> User:
        is_exists = self.user_repository.exist(email=dto.email)
        if is_exists:
            raise ApplicationException(f"ユーザーは既に登録されています email={dto.email}")

        user = self.user_repository.create(email=dto.email, password=dto.password)

        if user:
            return user

        # Userが存在しない場合は、新規作成する
        created_user = self.user_repository.create(email=dto.email)

        return created_user
