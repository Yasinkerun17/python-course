from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped ,mapped_column ,declarative_base, relationship, sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

Base = declarative_base()

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

class UserAssociation(Base):
    __tablename__ = "user_associations"
    id = Column(Integer, primary_key=True)
    
    follower_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    following = relationship("User", secondary="user_associations",
                             primaryjoin="UserAssociation.follower_id==User.id",
                             secondaryjoin="UserAssociation.following_id==User.id",
                             backref='followers')

    def __repr__(self):
        return f"<User: {self.name}>"

Base.metadata.create_all(engine)

user_1 = User(name="John")
user_2 = User(name="Rob")
user_3 = User(name="Kyle")

user_1.following.append(user_2)
user_2.following.append(user_1)
user_3.following.append(user_1)

# session.add_all([user_1, user_2, user_3])
# session.commit()

print(f"{user_1} is following: {user_1.following}")
print(f"{user_1} is being followed by: {user_1.followers}")