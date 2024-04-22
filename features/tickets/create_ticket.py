from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from data.database import Database
from models.ticket_model import Ticket
from startup import DependencyContainer

router = APIRouter()

class CreatedTicketResponse(BaseModel):
    id: int

@router.post("/")
@inject
def create_ticket(db: Database = Depends(Provide[DependencyContainer.db])) -> CreatedTicketResponse:
    with db.session() as session:
        ticket = Ticket()
        session.add(ticket)
        session.flush()

        ticket_id = ticket.Id
        session.commit()
        return CreatedTicketResponse(id=ticket_id)
