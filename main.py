from fastapi import FastAPI

from app.infrastructure.controller import anomalyRouter, loginRouter, logoutRouter

app = FastAPI()
app.include_router(loginRouter)
app.include_router(logoutRouter)
app.include_router(anomalyRouter)
