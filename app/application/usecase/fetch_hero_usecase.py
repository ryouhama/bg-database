from app.domain.repository_interface.hero_repository_interface import (
    HeroRepositoryInterface,
)


class FetchHeroUsecase:
    def __init__(self, hero_repository: HeroRepositoryInterface):
        self.hero_repository = hero_repository

    def execute(self) -> dict:
        dammy_url = "https://example.com"
        heros = self.hero_repository.fetch(dammy_url)
        return {"heros": [it.model_dump() for it in heros.items]}
