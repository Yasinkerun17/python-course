from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__="users"
    first_name:Mapped[str]
    last_name:Mapped[str]
    
    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.expression
    def full_name(cls):
        return cls.first_name + " " + cls.last_name
    
Base.metadata.create_all(engine)

# user1 = User(first_name="Yasin", last_name="Kerun")
# user2 = User(first_name="abc", last_name="tech")
# user3 = User(first_name="zeq", last_name="tech")

# session.add_all([user1, user2, user3])
# session.commit()

user = session.query(User).filter(User.full_name.like("abc%")).first()
print(f"{user.first_name} {user.last_name}")
print(user.full_name)
