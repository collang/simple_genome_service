from fastapi import FastAPI

from src.api.utils import add_app_routers
from src.api.routes import sequence

app = FastAPI()

add_app_routers(app, routers=[sequence.router])
