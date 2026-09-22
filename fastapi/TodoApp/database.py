from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

db = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db)
Session = sessionmaker(bind=engine)