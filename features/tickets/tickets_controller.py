from fastapi import APIRouter


router = APIRouter(prefix="/tickets", tags=["TicketsController"])

@router.get("/")
def get_tickets():
    pass