import pytest
from app.domain.entity.hero import Heros, Hero
from app.domain.value_object.hero_id import HeroId


class TestHeros:
    @pytest.fixture
    def create_hero(self):
        hero1 = Hero(
            id=HeroId.generate(1), name="test1", description="test1 description"
        )
        hero2 = Hero(
            id=HeroId.generate(2), name="test2", description="test2 description"
        )
        return hero1, hero2

    def test__find__idが一致するHeroドメインを返却すること(self, create_hero):
        hero1, hero2 = create_hero
        heros = Heros(items=[hero1, hero2])

        actual = heros.find(id=HeroId.generate(1))
        expected = Hero(
            id=HeroId.generate(1), name="test1", description="test1 description"
        )
        assert actual == expected

    def test__find__idが一致しない場合はNoneを返却すること(self, create_hero):
        hero1, hero2 = create_hero
        heros = Heros(items=[hero1, hero2])

        actual = heros.find(id=HeroId.generate(3))
        assert actual is None

    def test__find__idが一致するHeroドメインが複数存在する場合は先頭のドメインを返却すること(self):
        hero1 = Hero(
            id=HeroId.generate(1), name="test1", description="test1 description"
        )
        hero2_with_same_id = Hero(
            id=HeroId.generate(1), name="test2", description="test2 description"
        )
        heros = Heros(items=[hero1, hero2_with_same_id])

        actual = heros.find(id=HeroId.generate(1))
        expected = Hero(
            id=HeroId.generate(1), name="test1", description="test1 description"
        )
        assert actual == expected
