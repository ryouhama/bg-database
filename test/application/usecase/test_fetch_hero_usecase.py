from app.application.usecase.fetch_hero_usecase import FetchHeroUsecase
from app.domain.entity.hero import Heros, Hero
from app.domain.value_object.hero_id import HeroId
from test.mock.repository.mock_hero_repository import MockedHeroRepository


class TestFetchHeroUsecase:
    def test__execute__(self):
        mocked_repository = MockedHeroRepository()
        mocked_repository.return_value = Heros(
            items=[
                Hero(id=HeroId.generate(1), name="hero1", description="description1"),
                Hero(id=HeroId.generate(2), name="hero2", description="description2"),
            ]
        )

        usecase = FetchHeroUsecase(mocked_repository)

        actual = usecase.execute()

        expected = {
            "heros": [
                {
                    "id": 1,
                    "name": "hero1",
                    "description": "description1",
                },
                {
                    "id": 2,
                    "name": "hero2",
                    "description": "description2",
                },
            ]
        }
        assert actual == expected
