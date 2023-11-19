from app.domain.entity.anomaly import Anomaly
from app.domain.value_object.anomaly_id import AnomalyId
from app.infrastructure.repository.anomaly_repository import AnomalyRepository


class TestAnomalyRepository:
    def test__fetch__(self):
        actual = AnomalyRepository().fetch()

        expected = [
            Anomaly(
                id=AnomalyId.generate(1),
                name="おっと、全部アンデット！",
                description="酒場には、アンデットのみ出場。",
            )
        ]
        assert actual == expected
