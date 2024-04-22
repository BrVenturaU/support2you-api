from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from data.database import Database
from models.ticket_model import Ticket, TicketStatus
from startup import DependencyContainer

router = APIRouter()

class UpdateTicketRequest(BaseModel):
    status: TicketStatus

class CreatedTicketResponse(BaseModel):
    id: int

@router.put("/{id}")
@inject
def update_ticket_status(id: int, ticket_request: UpdateTicketRequest, db: Database = Depends(Provide[DependencyContainer.db])):
    with db.session() as session:
        ticket = session.query(Ticket).filter(Ticket.Id == id).first()
        if ticket == None:
            return "Not found"
        
        ticket.Status = ticket_request.status
        session.flush()

        ticket_id = ticket.Id
        session.commit()
        
        return CreatedTicketResponse(id=ticket_id)
