from app.domain.entity.hero import Hero, Heros
from app.domain.value_object.hero_id import HeroId
from app.domain.repository_interface.hero_repository_interface import (
    HeroRepositoryInterface,
)
from app.infrastructure.repository.internal.google_spread_sheet_repository import (
    GoogleSpreadSheetRepository,
)


class HeroRepository(HeroRepositoryInterface):
    def fetch(self, url: str) -> Heros:
        google_spread_sheet_repository = GoogleSpreadSheetRepository()
        sheet = google_spread_sheet_repository.fetch_by_url(url)
        return sheet

    def save(self, hero: Hero) -> Hero:
        ...
        return super().save(hero)

    def delete(self, id: HeroId) -> None:
        ...
        return super().delete(id)
