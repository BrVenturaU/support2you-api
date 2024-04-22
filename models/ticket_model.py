import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from data.database import Base


class TicketStatus(enum.Enum):
    NUEVO = 1
    ABIERTO = 2
    PENDIENTE = 3
    ESPERA = 4
    RESUELTO = 5

class Ticket(Base):
    __tablename__ = "Tickets"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Status: Mapped[TicketStatus] = mapped_column(Enum(TicketStatus), default=TicketStatus.NUEVO)