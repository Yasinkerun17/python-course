from time import perf_counter

from sqlalchemy import (Column, ForeignKey, Integer, create_engine, String, Text)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url, echo=True) # important

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post",lazy="selectin", backref="user")
    
    def __repr__(self):
        return f"<user {self.name}, >"
    
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    
    def __repr__(self):
        return f"<Post {self.id}, {self.content}>"

Base.metadata.create_all(engine)  

# new_user = User(name="yasin",
#              posts=[
#                  Post(content=f"this is content for {x}")
#                  for x in range(1,5)
#              ]
#         )      

# session.add_all(
#     [
#         User(
#             name=f"User {y}",
#             posts=[
#                 Post(
#                     content=f"This is the content for {y * 5 + x}"
#                 )
#                 for x in range(50)
#             ],
#         )
#             for y in range(10_000)
#     ]
# )

session.commit()

start = perf_counter()
users = session.query(User).all()

print("Accessing all User posts")

for user in users:
    user.posts
    
print(f"Done in: {perf_counter() - start}")