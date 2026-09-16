from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.exc import InvalidRequestError


db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    
class Parent(Base):
    __tablename__ = "parents"
    children: Mapped[list['Child']] = relationship(back_populates='parent',cascade="save-update, expunge")
    def __repr__(self):
        return f"<Parent id: {self.id}, Children : {self.children}>"
    
class Child(Base):
    __tablename__ = "children"
    parent_id:Mapped[int] = mapped_column(ForeignKey("parents.id"))
    parent:Mapped[Parent] = relationship(back_populates="children")
    
    def __repr__(self):
        return f"<Child - parent_id: {self.parent_id}, child_id: {self.id}>"


Base.metadata.create_all(engine)

# parent = Parent(children=[Child()])
# session.add(parent)
# session.commit()
parent = session.query(Parent).filter_by(id=1).first()
session.expunge(parent)
assert parent not in session
print(parent)

# try:
#     print(parent.children[0])
# except:
#     print("parent.children are not in this session")
