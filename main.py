from fastapi import FastAPI

from app.infrastructure.controller import loginRouter, logoutRouter, anomalyRouter

app = FastAPI()
app.include_router(loginRouter)
app.include_router(logoutRouter)
app.include_router(anomalyRouter)
