from app.domain.entity.base import Entity
from app.domain.value_object.anomaly_id import AnomalyId


class Anomaly(Entity):
    """
    異常
    """

    id: AnomalyId
    name: str
    description: str
