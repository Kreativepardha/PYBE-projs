from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceed _handler
from slowapi.util import get_remote_address
from app.routes import router
from app.utils import init_redis
from loguru import logger



app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.add_exception_handler(429, _rate_limit_exceeded_handler)

logger.add("app.log", rotation= "500 MB")

redis = init_redis()


app.include_router(router)

@app.on_event("startup")
async def on_startup():
    logger.info("APplication is starting")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("application is shutting down...")

