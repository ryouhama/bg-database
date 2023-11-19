from typing import Optional
from app.domain.entity.base import Entity
from app.domain.value_object import UserId, UserProfileId


class UserProfile(Entity):
    id: UserProfileId
    user_id: UserId
    name: str
    icon_path: Optional[str]
