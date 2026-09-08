from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped ,mapped_column ,declarative_base, relationship, sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

Base = declarative_base()

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address",back_populates="user", uselist=False)
    
class Address(Base):
    __tablename__ = "address"
        
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="address")

Base.metadata.create_all(engine)

# new_user = User(name="John Doe")
# new_address = Address(email="john.example.com", user=new_user)
# session.add(new_user)
# session.add(new_address)

session.commit()


# print(new_user.name)
# print(new_address.email)
# print(new_user.address.email)
# print(new_address.user.name)

user = session.query(User).filter_by(name="John Doe").first()

print(f"username={user.name} email={user.address.email} ")