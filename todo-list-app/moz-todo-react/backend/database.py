# database.py
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///./sqlite.db", echo=True)


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


DatabaseSession = Annotated[Session, Depends(get_session)]

