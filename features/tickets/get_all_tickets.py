from pydantic import BaseModel
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from data.database import Database
from models.ticket_model import Ticket
from startup import DependencyContainer

class TicketResponse(BaseModel):
    id: int
    status: str

router = APIRouter()

@router.get("/")
@inject
def get_all_tickets(db: Database = Depends(Provide[DependencyContainer.db])) -> list[TicketResponse]:
    with db.session() as session:
        tickets = session.query(Ticket).all()
        return [TicketResponse(id=el.Id, status=el.Status.name) for el in tickets]
        