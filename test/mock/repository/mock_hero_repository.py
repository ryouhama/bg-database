from typing import Any

from app.domain.entity.hero import Heros
from app.infrastructure.repository.hero_repository import HeroRepository


class MockedHeroRepository(HeroRepository):
    return_value: Any

    def fetch(self, url: str) -> Heros:
        return self.return_value
