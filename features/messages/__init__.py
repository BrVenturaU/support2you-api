from fastapi import APIRouter
from . import get_ticket_messages


messages_controller = APIRouter(
    prefix="/tickets/{ticket_id}/messages",
    tags=["MessagesController", "TicketsController"],
)
messages_controller.include_router(get_ticket_messages.router)
