from typing import Optional
from app.domain.entity.base import Entity
from app.domain.value_object.hero_id import HeroId


class Heros:
    """
    バトルグラウンドに登場するヒーローの集約
    """

    items: list["Hero"]

    def find(self, id: HeroId) -> Optional["Hero"]:
        if len(result := filter(lambda hero: hero.id == id, self.items)) >= 1:
            return result[0]
        return None

    def find_by_name(self, name: str) -> Optional["Hero"]:
        if len(result := filter(lambda hero: hero.name == name, self.items)) >= 1:
            return result[0]
        return None


class Hero(Entity):
    """
    バトルグラウンドに登場するヒーロー
    """

    id: HeroId
    name: str
    description: str
