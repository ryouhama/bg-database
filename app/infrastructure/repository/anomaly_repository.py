from app.infrastructure.db import TableSchema, get_client
from app.domain.repository_interface.anomaly_repository_interface import (
    AnomalyRepositoryInterface,
)
from app.domain.entity.anomaly import Anomaly
from app.domain.value_object.anomaly_id import AnomalyId


class AnomalyRepository(AnomalyRepositoryInterface):
    client = get_client()

    async def fetch(self) -> list[Anomaly]:
        response = (
            await self.client.table(TableSchema.ANOMALY)
            .select("id, name, description")
            .execute()
        )

        return [
            Anomaly(
                id=AnomalyId(it["id"]),
                name=it["name"],
                description=it["description"],
            )
            for it in response.data
        ]

    async def update(self, anomaly: Anomaly) -> Anomaly:
        response = (
            await self.client.table(TableSchema.ANOMALY)
            .update({"name": anomaly.name})
            .eq("id", anomaly.id)
            .execute()
        )
        return anomaly.model_rebuild(name=response.data["name"])

    async def delete(self, id: AnomalyId) -> None:
        await self.client.table(TableSchema.ANOMALY).delete().eq("id", id).execute()
