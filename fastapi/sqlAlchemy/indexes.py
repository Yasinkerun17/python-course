from sqlalchemy import Integer, String, create_engine, Index
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)
    
class User(Base):
    __tablename__="users"
    name:Mapped[str] = mapped_column()
    email:Mapped[str]
    

Base.metadata.reflect(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

user_name_index = Index("ix_user_name", User.name)
user_name_index.create(bind=engine, checkfirst=True)
user_name_index.create(bind=engine,checkfirst=True)

for name, table in Base.metadata.tables.items():
    print(f"\ntable: {name}")
    indexes = list(table.indexes)
    if len(indexes) < 1:
        print("No Indexes")
        
    for index in indexes:
        print(f"Index name: {index.name}")
        print(f"Columns: {', '.join([column.name for column in index.columns])}")

