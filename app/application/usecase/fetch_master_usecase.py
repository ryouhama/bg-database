from app.domain.repository_interface import (
    AnomalyRepositoryInterface,
    HeroRepositoryInterface,
)


class FetchMasterUsecase:
    def __init__(
        self,
        anomaly_repository: AnomalyRepositoryInterface,
        hero_repository: HeroRepositoryInterface,
    ) -> None:
        self.anomaly_repository = anomaly_repository
        self.hero_repository = hero_repository

    def execute(self):
        anomalies = self.anomaly_repository.fetch()
        heros = self.hero_repository.fetch()

        return {
            "anomalies": [it.model_dump() for it in anomalies],
            "heros": [it.model_dump() for it in heros],
        }
