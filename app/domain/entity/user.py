from app.domain.entity.base import Entity
from app.domain.value_object.user_id import UserId


class User(Entity):
    id: UserId
