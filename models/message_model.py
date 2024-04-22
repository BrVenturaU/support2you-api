import enum
from sqlalchemy import ForeignKey, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from data.database import Base


class MessageRole(enum.Enum):
    system = "system"
    assistant = "assistant"
    user = "user"

class Message(Base):
    __tablename__ = "Messages"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Content: Mapped[str] = mapped_column(String)
    Role: Mapped[MessageRole] = mapped_column(Enum(MessageRole))
    TicketId: Mapped[int] = mapped_column(ForeignKey("Tickets.Id"))