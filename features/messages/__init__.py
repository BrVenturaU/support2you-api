from fastapi import APIRouter
from . import (
    get_ticket_messages,
    add_message_to_ticket
)


messages_controller = APIRouter(
    prefix="/tickets/{ticket_id}/messages",
    tags=["MessagesController", "TicketsController"],
)
messages_controller.include_router(get_ticket_messages.router)
messages_controller.include_router(add_message_to_ticket.router)
