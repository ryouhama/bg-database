from app.infrastructure.db import TableSchema, get_client
from app.domain.repository_interface.anomaly_repository_interface import (
    AnomalyRepositoryInterface,
)
from app.domain.entity.anomaly import Anomaly
from app.domain.value_object.anomaly_id import AnomalyId


class AnomalyRepository(AnomalyRepositoryInterface):
    client = get_client()

    def fetch(self) -> list[Anomaly]:
        response = (
            self.client.table(TableSchema.ANOMALY.value)
            .select("id,name,description")
            .execute()
        )

        return [
            Anomaly(
                id=AnomalyId.generate(it["id"]),
                name=it["name"],
                description=it["description"],
            )
            for it in response.data
        ]

    def update(self, anomaly: Anomaly) -> Anomaly:
        response = (
            self.client.table(TableSchema.ANOMALY)
            .update({"name": anomaly.name})
            .eq("id", anomaly.id)
            .execute()
        )
        return anomaly.model_rebuild(name=response.data["name"])

    def delete(self, id: AnomalyId) -> None:
        self.client.table(TableSchema.ANOMALY).delete().eq("id", id).execute()
