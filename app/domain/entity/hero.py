from typing import Optional
from app.domain.entity.base import Entity
from app.domain.value_object.hero_id import HeroId


class Heros:
    """
    バトルグラウンドに登場するヒーローの集約
    """

    items: list["Hero"]

    def __init__(self, items: list["Hero"]) -> None:
        self.items = items

    def find(self, id: HeroId) -> Optional["Hero"]:
        if len(result := list(filter(lambda hero: hero.id == id, self.items))) >= 1:
            return result[0]
        return None


class Hero(Entity):
    """
    バトルグラウンドに登場するヒーロー
    """

    id: HeroId
    name: str
    description: str
