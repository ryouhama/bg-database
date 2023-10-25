from abc import ABC, abstractmethod
from app.domain.entity.hero import Heros, Hero
from app.domain.value_object.hero_id import HeroId


class HeroRepositoryInterface(ABC):
    """
    バトルグラウンドに登場するヒーローに関するリポジトリー
    """

    @abstractmethod
    def fetch(self) -> Heros:
        raise NotImplementedError

    @abstractmethod
    def save(self, hero: Hero) -> Hero:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: HeroId) -> None:
        raise NotImplementedError
