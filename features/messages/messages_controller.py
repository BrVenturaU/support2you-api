from fastapi import APIRouter


router = APIRouter(prefix="/tickets/{ticket_id}/messages", tags=["MessagesController", "TicketsController"])

@router.get("/")
def get_messages(ticket_id: int):
    pass