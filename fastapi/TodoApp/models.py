from sqlalchemy import  ForeignKey
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True, index=True)


class User(Base):
    __tablename__ = "users"
    email:Mapped[str] = mapped_column(unique=True)
    username:Mapped[str] = mapped_column(unique=True)
    first_name:Mapped[str]
    last_name:Mapped[str]
    hashed_password:Mapped[str]
    is_active:Mapped[bool] = mapped_column(default=True)
    role:Mapped[str]
    # todos:Mapped[list["Todos"]] = relationship("Todos", back_populates="user", uselist=True)


class Todos(Base):
    __tablename__ = "todos"
    title:Mapped[str]
    description:Mapped[str]
    priority:Mapped[int]
    complete:Mapped[bool]
    owner_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    # user = relationship("User",back_populates="todos", uselist=False)
    
    def __repr__(self):
        return "< title: {self.title}, description: {self.description}, Complete: {self.complete}>"
    