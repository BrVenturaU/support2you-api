from typing import Union
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from data.database import Database
from models.ticket_model import Ticket, TicketStatus
from startup import DependencyContainer
from schema.base import ApiResponse

router = APIRouter()


class UpdateTicketRequest(BaseModel):
    status: TicketStatus


class CreatedTicketResponse(BaseModel):
    id: int


@router.put(
    "/{id}", response_model=ApiResponse, responses={404: {"model": ApiResponse}}
)
@inject
def update_ticket_status(
    id: int,
    ticket_request: UpdateTicketRequest,
    db: Database = Depends(Provide[DependencyContainer.db]),
) -> Union[JSONResponse, ApiResponse, None]:
    with db.session() as session:
        ticket = session.query(Ticket).filter(Ticket.Id == id).first()
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

        ticket.Status = ticket_request.status
        session.commit()

        return ApiResponse(
            message="El estado del ticket ha sido actualizado.",
            data=UpdateTicketRequest(status=ticket_request.status),
        )
