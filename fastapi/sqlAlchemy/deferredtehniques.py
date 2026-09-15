from sqlalchemy import Integer, create_engine, Column, String, ForeignKey, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, defer, deferred, undefer_group

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url, echo=True)

Session =  sessionmaker(bind=engine)

session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    
class User(Base):
    __tablename__= "users"
    
    nickname: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = deferred(mapped_column(String), group="names")
    last_name: Mapped[str] = deferred(Column(String), group="names")
    other_value: Mapped[str] = mapped_column(String, deferred=True, deferred_group="others")
    
    def __repr__(self):
        return f"id: {self.id}, nickname: {self.nickname}"
    
Base.metadata.create_all(engine)
    
# user = User(nickname="yasin", first_name="Yasin", last_name="Kerun", other_value="other")
# session.add(user)

session.commit()

# user = session.scalar(select(User))

user = session.query(User).options().first()

print(user)
print(user.first_name)
print(user.last_name)
print(user.other_value)

