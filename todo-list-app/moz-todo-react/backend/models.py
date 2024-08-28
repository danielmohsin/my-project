# models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False, server_default="false")

