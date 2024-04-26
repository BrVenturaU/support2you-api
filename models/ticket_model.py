import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.database import Base
from .message_model import Message as MessageModel

class TicketStatus(enum.Enum):
    NUEVO = "NUEVO"
    ABIERTO = "ABIERTO"
    PENDIENTE = "PENDIENTE"
    ESPERA = "ESPERA"
    RESUELTO = "RESUELTO"

class Ticket(Base):
    __tablename__ = "Tickets"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Status: Mapped[TicketStatus] = mapped_column(Enum(TicketStatus), default=TicketStatus.NUEVO)
    Messages: Mapped[list[MessageModel]] = relationship()