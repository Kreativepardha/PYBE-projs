from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceed _handler

app = FastAPI()


app.include_router(router)


