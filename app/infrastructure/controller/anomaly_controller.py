from fastapi import APIRouter
from injector import Injector

from app.application.usecase.fetch_master_usecase import FetchMasterUsecase
from app.domain.repository_interface import (
    AnomalyRepositoryInterface,
    HeroRepositoryInterface,
)
from app.infrastructure.db import Client, get_client
from app.infrastructure.repository.anomaly_repository import AnomalyRepository
from app.infrastructure.repository.hero_repository import HeroRepository

router = APIRouter()


injector = Injector()
injector.binder.bind(AnomalyRepositoryInterface, to=AnomalyRepository())
injector.binder.bind(HeroRepositoryInterface, to=HeroRepository())


@router.get("/anomaly")
async def fetch():
    usecase = injector.get(FetchMasterUsecase)
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
