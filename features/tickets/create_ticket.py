from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from data.database import Database
from models.ticket_model import Ticket
from startup import DependencyContainer
from schema.base import ApiResponse

router = APIRouter()

class CreatedTicketResponse(BaseModel):
    id: int

@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create_ticket(db: Database = Depends(Provide[DependencyContainer.db])) -> ApiResponse[CreatedTicketResponse]:
    with db.session() as session:
        ticket = Ticket()
        session.add(ticket)
        session.flush()

        ticket_id = ticket.Id
        session.commit()
        return ApiResponse(
            message="El ticket ha sido creado exitosamente.",
            code=status.HTTP_201_CREATED,
            data=CreatedTicketResponse(id=ticket_id)
        )
