from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped ,mapped_column ,declarative_base, relationship, sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

Base = declarative_base()

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))

class User(BaseModel):
    __tablename__ = "users"
    
    username = Column(String)
    following = relationship("User", secondary="following_association",
                             primaryjoin=("following_association.c.user_id==User.id"),
                             secondaryjoin=("following_association.c.following_id==User.id"))
    
    def __repr__(self):
        return f"<users(id={self.id}, username={self.username}, following={self.following})>"

Base.metadata.create_all(engine)
