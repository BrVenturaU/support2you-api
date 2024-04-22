from pydantic import BaseModel
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from data.database import Database
from models.ticket_model import Ticket
from startup import DependencyContainer
from schema.base import ApiResponse

class TicketResponse(BaseModel):
    id: int
    status: str

router = APIRouter()

@router.get("/")
@inject
def get_all_tickets(db: Database = Depends(Provide[DependencyContainer.db])) -> ApiResponse[list[TicketResponse]]:
    with db.session() as session:
        tickets = session.query(Ticket).all()
        tickets_response = [TicketResponse(id=el.Id, status=el.Status.name) for el in tickets]
        return ApiResponse(
            message="Listado de tickets obtenido correctamente.",
            data=tickets_response
        )
        