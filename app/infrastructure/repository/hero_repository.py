from app.domain.entity import Hero, Heros
from app.domain.repository_interface.hero_repository_interface import (
    HeroRepositoryInterface,
)
from app.domain.value_object import HeroId
from app.infrastructure.db import TableSchema, get_client


class HeroRepository(HeroRepositoryInterface):
    client = get_client()

    def fetch(self) -> Heros:
        res = (
            self.client.table(TableSchema.HERO.value)
            .select("id, name, description")
            .execute()
        )

        return Heros(
            [
                Hero(
                    id=HeroId(row["id"]),
                    name=row["name"],
                    description=row["description"],
                )
                for row in res.data
            ]
        )

    def save(self, hero: Hero) -> Hero:
        ...
        return super().save(hero)

    def delete(self, id: HeroId) -> None:
        ...
        return super().delete(id)
