from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from data.database import Database
from models.ticket_model import Ticket
from models.message_model import Message, MessageRole
from startup import DependencyContainer
from schema.base import ApiResponse

router = APIRouter()

class MessageRequest(BaseModel):
    content: str

class CreatedMessageResponse(BaseModel):
    id: int
    content: str

class MessageResponse(BaseModel):
    user: CreatedMessageResponse
    assistant: CreatedMessageResponse


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def add_message_to_ticket(
    ticket_id: int,
    message_request: MessageRequest,
    db: Database = Depends(Provide[DependencyContainer.db]),
) -> ApiResponse[MessageResponse]:
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

        user_message = Message(
            Content=message_request.content, Role=MessageRole.user, TicketId=ticket.Id
        )

        # TODO: Send user message to assistant and get that response to store it.
        # Get the prior messages to recall the conversation context.
        # Validate if it is the first message to add the system role.
        # Just add the newly created message.

        ticket.Messages.append(user_message)
        session.flush()

        user_message_response = CreatedMessageResponse(
            id=user_message.Id, content=user_message.Content
        )
        assistant_message_response = CreatedMessageResponse(
            id=0, content="assistant message."
        )

        session.commit()
        return ApiResponse(
            message="Mensaje procesado con exito.",
            code=status.HTTP_201_CREATED,
            data=MessageResponse(
                user=user_message_response, assistant=assistant_message_response
            ),
        )
