from fastapi import APIRouter
from . import get_all_tickets

tickets_controller = APIRouter(prefix="/tickets", tags=["TicketsController"])
tickets_controller.include_router(get_all_tickets.router)
    