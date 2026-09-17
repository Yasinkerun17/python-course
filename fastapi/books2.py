from typing import Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, ConfigDict, Field
from starlette import status
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship, DeclarativeBase

db_url = "postgresql://postgres:postgres@localhost:5432/Database1"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
app = FastAPI()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Book(Base):
    __tablename__ = "books"
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    rating: Mapped[int]
    published_date: Mapped[int]
    
    # def __init__(self, id, title, author, description, rating, published_date):
    #     self.id = id
    #     self.title = title
    #     self.author = author
    #     self.description = description
    #     self.rating = rating
    #     self.published_date = published_date


class BookRequest(BaseModel):
    # id: Optional[int] = Field(description="id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date : int = Field(gt=1999, lt=2031)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A New Book",
                "author": "Yasin",
                "description": "A new book",
                "rating": 5,
                "published_date": 2025
            }
        }
    }


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    model_config = ConfigDict(from_attributes=True)

Base.metadata.create_all(engine)
    
# session = Session()
# Book1 = Book(id=1,title="Computer Science Pro", author="Yasin", description="a good book",rating=5, published_date=2010)
# session.add(Book1)
# session.commit()


@app.get("/books", response_model=list[BookResponse], status_code=status.HTTP_200_OK)
def get_all_books():
    db = Session()
    try:
        return db.query(Book).all()
    finally:
        db.close()

@app.get("/books/{book_id}",response_model=BookResponse, status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    session = Session()
    book_list = session.query(Book).filter(Book.id == book_id).first()
    
    if not book_list:
        raise HTTPException(status_code=404,detail="Book not found")
    
    try:
        return book_list
    finally:
        session.close()


@app.get("/books/",response_model=list[BookResponse], status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    session = Session()
    book_list = session.query(Book).filter(Book.rating == book_rating).all()
    if not book_list:
        raise HTTPException(status_code=404,detail="Book not found")
    try:
        return book_list
    finally:
        session.close()
      
@app.get("/books/publish/",response_model=list[BookResponse] , status_code=status.HTTP_200_OK)
async def get_Book_by_Date(published_date: int = Query(gt=1999, lt=2031)):
    db = Session()
    books_requested = db.query(Book).filter(Book.published_date == published_date).all()
    if not books_requested:
            raise HTTPException(status_code=404,detail="Book not found")
    try:
        return books_requested
    finally:
        db.close()


@app.post("/create-book",response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    session = Session()
    try:
        book = Book(**book_request.model_dump())
        session.add(book)
        session.commit()
        
        return book
    finally:
        session.close()

    
# def find_book_id(book: Book):
#     if (len(BOOKS) > 0):
#         book.id = BOOKS[-1].id + 1
#     else:
#         book.id = 1
#     return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def Update_Book(book: BookRequest):
    session = Session()
    
    book_updated = session.query(Book).filter(Book.id == book.id).first()
       
    if not book_updated:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_updated.title = book.title
    book_updated.author = book.author
    book_updated.description = book.description
    book_updated.rating = book.rating
    book_updated.published_date = book.published_date
    session.commit()
    session.close()

    

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def Delete_Book(book_id: int = Path(gt=0)):
    db = Session()
    book_changed = db.query(Book).filter(Book.id == book_id).first()
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
    
    try:
        db.delete(book_changed)
        db.commit()
    finally:
        db.close()
        