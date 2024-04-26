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
from services.chat_service import ChatService, PromptMessage

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
    chat_service: ChatService = Depends(Provide[DependencyContainer.chat_service]),
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

        messages = [
            *[PromptMessage(el.Role, el.Content) for el in ticket.Messages],
            PromptMessage(MessageRole.user, message_request.content),
        ]

        assistant_answer = chat_service.answer(messages)

        user_message = Message(
            Content=message_request.content, Role=MessageRole.user, TicketId=ticket.Id
        )
        assistant_message = Message(
            Content=assistant_answer, Role=MessageRole.assistant, TicketId=ticket.Id
        )

        ticket.Messages.append(user_message)
        ticket.Messages.append(assistant_message)
        session.flush()

        user_message_response = CreatedMessageResponse(
            id=user_message.Id, content=user_message.Content
        )
        assistant_message_response = CreatedMessageResponse(
            id=assistant_message.Id, content=assistant_message.Content
        )

        session.commit()

        return ApiResponse(
            message="Mensaje procesado con exito.",
            code=status.HTTP_201_CREATED,
            data=MessageResponse(
                user=user_message_response, assistant=assistant_message_response
            ),
        )
