from fastapi import APIRouter
from injector import Injector, inject
from app.infrastructure.repository.anomaly_repository import AnomalyRepository
from app.infrastructure.repository.hero_repository import HeroRepository
from app.application.usecase.fetch_master_usecase import FetchMasterUsecase

router = APIRouter()


@router.get("/anomaly")
async def fetch():
    usecase = FetchMasterUsecase(
        anomaly_repository=AnomalyRepository(), hero_repository=HeroRepository()
    )
    return usecase.execute()


@router.post("/anomaly")
async def create():
    return ...


@router.put("/anomaly/{anomaly_id}")
async def update(anomaly_id: int):
    return ...


@router.delete("/anomaly/{anomaly_id}")
async def delete(anomaly_id: int):
    return ...
