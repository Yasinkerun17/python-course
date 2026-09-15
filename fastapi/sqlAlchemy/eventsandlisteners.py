from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped, DeclarativeBase, Mapper
from sqlalchemy.engine import Connection

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)
    
class User(Base):
    __tablename__="users"
    name: Mapped[str]
    email: Mapped[str]
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def insert_user_listener(mapper: Mapper, connection: Connection, target: User):
    print(f"Inserting user: {target.name}")
    
event.listen(User, 'before_insert', insert_user_listener)

# for x in range(1,10):
#     user = User(name=f"user {x}", email=f"user_{x}@example.com")
#     session.add(user)
    
@event.listens_for(User, 'before_update')
def audit_user_update(mapper: Mapper, connection: Connection, target: User):
    stmt = text("select email from users where id = :user_id")
    old_email = connection.scalar(stmt, {"user_id": target.id})
    new_email = target.email
    if old_email != new_email:
        print(f"email changed for user {target.id} {target.email}")
    else:
        print("email not updated")

user = session.query(User).filter_by(name = "user 1").first()
user.email = "user_updated@example.com"

session.commit()
