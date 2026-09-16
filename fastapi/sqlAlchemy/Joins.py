from typing import Optional

from sqlalchemy import Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, relationship

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine= create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
class Address(Base):
    __tablename__ = "address"
    
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'))
    data: Mapped[str]
    
    def __repr__(self):
        return f"< Address: {self.data}>"

class User(Base):
    __tablename__= "users"
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    address:Mapped[Address] = relationship()

    def __repr__(self):
        return f"< User: {self.first_name} {self.last_name}"

Base.metadata.create_all(engine)


# address_1 = Address(data="1234 street address")

# address_2 = Address(data="5678 non existence address")

# address_3 = Address(data="910 extra address")

# user1 = User(
#     first_name="yasin",
#     last_name="Kerun",
#     address=address_1,
# )

# user2 = User(
#     first_name="super",
#     last_name="Man",
#     address=None,
# )

# session.add_all([address_1, address_2, address_3, user1, user2])

# session.commit()

# result = session.query(User,Address).join(Address).all()

# print("Inner JOIN")

# result = session.query(User,Address).join(Address).filter(User.address==None, Address.user_id==None).all()

# print("Outer JOIN")

# result = session.query(User,Address).outerjoin(User).all()

# print("\n Left Outer JOIN")
# print(result)

# result = session.query(User,Address).outerjoin(User).all()

# print("\n Right Outer JOIN")
# print(result)

left_join = session.query(User,Address).outerjoin(Address)

right_join = session.query(User,Address).outerjoin(User)

full_join = left_join.union(right_join)

print("\n Right Outer JOIN")
print(full_join.all())
