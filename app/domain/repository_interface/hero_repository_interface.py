from abc import ABC, abstractmethod

from app.domain.entity import Hero, Heros
from app.domain.value_object import HeroId


class HeroRepositoryInterface(ABC):
    """
    バトルグラウンドに登場するヒーローに関するリポジトリー
    """

    @abstractmethod
    def fetch(self, url: str) -> Heros:
        raise NotImplementedError

    @abstractmethod
    def save(self, hero: Hero) -> Hero:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: HeroId) -> None:
        raise NotImplementedError
