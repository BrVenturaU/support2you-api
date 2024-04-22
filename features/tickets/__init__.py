from fastapi import APIRouter
from . import (
    get_all_tickets,
    create_ticket,
    update_ticket_status
)

tickets_controller = APIRouter(prefix="/tickets", tags=["TicketsController"])
tickets_controller.include_router(get_all_tickets.router)
tickets_controller.include_router(create_ticket.router)
tickets_controller.include_router(update_ticket_status.router)
    