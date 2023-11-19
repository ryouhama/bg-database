from app.domain.entity import Hero, Heros
from app.domain.repository_interface.hero_repository_interface import (
    HeroRepositoryInterface,
)
from app.domain.value_object import HeroId


class HeroRepository(HeroRepositoryInterface):
    def fetch(self) -> Heros:
        ...

    def save(self, hero: Hero) -> Hero:
        ...
        return super().save(hero)

    def delete(self, id: HeroId) -> None:
        ...
        return super().delete(id)
