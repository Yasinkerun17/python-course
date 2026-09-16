from sqlalchemy import Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = "users"
    name:Mapped[str]
    posts:Mapped[list["Post"]] = relationship(backref="user", lazy="select")
    
    def __repr__(self):
        return f"<User {self.name}>"
    
class Post(Base):
    __tablename__="posts"
    active:Mapped[bool] = mapped_column(default=True)
    users_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    Detail:Mapped["Detail"] = relationship(backref="post", lazy="select")
    
    @classmethod    
    def is_active(cls):
        return cls.active == True
    
    def __repr__(self):
        return f"<Post {self.id}, {self.Detail}>"
    
class Detail(Base):
    __tablename__="details"
    content:Mapped[str]
    post_id:Mapped[int] = mapped_column(ForeignKey("posts.id"))
    
    def __repr__(self):
        return f"< id: {self.id},content: {self.content}>"
    
Base.metadata.create_all(engine)

if __name__ == "__main__":
    user1 = User(name="Yasin")
    user1.posts = [
        Post(Detail=Detail(content="This is content of post 1")),
        Post(Detail=Detail(content="This is content of post 2"), active=True),
    ]
    
    user2 = User(name="Sam")
    user2.posts = [
            Post(Detail=Detail(content="This is content of post 1 of sam")),
            Post(Detail=Detail(content="This is content of post 2 of sam")),
        ]
    session.add_all([user1, user2])
    session.commit()
    
