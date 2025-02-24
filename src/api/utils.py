from tkinter import W
from typing import List
from fastapi import ApiRouter, FastAPI


def add_app_routers(app: FastAPI, routers: List[ApiRouter]):
    for router in routers:
        app.include_router(router=router)