from pydantic import BaseModel
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from data.database import Database
from models.ticket_model import Ticket
from models.message_model import MessageRole
from startup import DependencyContainer
from schema.base import ApiResponse


class MessageResponse(BaseModel):
    id: int
    content: str
    role: MessageRole


class TicketMessagesResponse(BaseModel):
    id: int
    status: str
    messages: list[MessageResponse]


router = APIRouter()


@router.get("/", responses={404: {"model": ApiResponse}})
@inject
def get_all_tickets_messages(
    ticket_id: int, db: Database = Depends(Provide[DependencyContainer.db])
) -> ApiResponse[TicketMessagesResponse]:
    with db.session() as session:
        ticket = session.query(Ticket).filter(Ticket.Id == ticket_id).first()
        if ticket == None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=jsonable_encoder(
                    ApiResponse(
                        code=status.HTTP_404_NOT_FOUND,
                        message="El ticket no ha sido encontrado.",
                    )
                ),
            )
        messages = [
            MessageResponse(id=el.Id, content=el.Content, role=el.Role)
            for el in ticket.Messages
        ]
        return ApiResponse(
            message="Listado de mensajes del ticket obtenidos correctamente.",
            data=TicketMessagesResponse(
                id=ticket.Id, status=ticket.Status, messages=messages
            ),
        )
