from typing import Iterator
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker, Session

class Base(DeclarativeBase):
    pass

class Database:
    def __init__(self, connection: str):
        self._engine = create_engine(connection)
        self._session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            )
        )
    
    @contextmanager
    def session(self) -> Iterator[Session]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            # TODO: Add logguer
            session.rollback()
            raise
        finally:
            print("Closed connection")
            session.close()