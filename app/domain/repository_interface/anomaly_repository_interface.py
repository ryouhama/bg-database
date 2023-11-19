from abc import ABC, abstractmethod

from app.domain.entity import Anomaly
from app.domain.value_object import AnomalyId


class AnomalyRepositoryInterface(ABC):
    """
    バトルグラウンドに登場するヒーローに関するリポジトリー
    """

    @abstractmethod
    def fetch(self) -> list[Anomaly]:
        raise NotImplementedError

    @abstractmethod
    def create(self, anomaly: Anomaly) -> Anomaly:
        raise NotImplementedError

    @abstractmethod
    def update(self, anomaly: Anomaly) -> Anomaly:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: AnomalyId) -> None:
        raise NotImplementedError
