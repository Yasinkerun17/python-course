from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
        {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
        {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
        {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
        {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
        {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
        {'title': 'Title six', 'author': 'Author two', 'category': 'math'},
]

@app.get("/")
async def first_page():
        return ("Hello Yasin")

@app.get("/books")
async def read_all_books():
        all_books = []
        for book in BOOKS:
                all_books.append(book)
        return all_books

@app.get("/books/{book_title}")
async def get_book(book_title: str):
        for book in BOOKS:
                if book.get('title').casefold() == book_title.casefold():
                        return book

@app.get("/books/")
async def get_book_by_category(category: str):
        books_to_return = []
        for book in BOOKS:
                if book.get('category').casefold() == category.casefold():
                                books_to_return.append(book)
        return books_to_return
 
@app.get("/books/byauthor/")
async def get_books_by_author(author_name: str):
        books_list = []
        for book in BOOKS:
                if book.get("author").casefold() == author_name.casefold():
                        books_list.append(book)
        return books_list
 
@app.get("/books/{book_author}/")
async def get_book_by_author_and_category(book_author: str, category: str):
        books_to_return = []
        
        for book in BOOKS:
                if book.get('author').casefold() == book_author.casefold() and \
                        book.get('category').casefold() == category.casefold():
                        books_to_return.append(book)
                
        return books_to_return



@app.post("/books/create_book")
async def create_book(new_book=Body()):
        BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
        for i in range(len(BOOKS)):
                if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
                        BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
        for i in range(len(BOOKS)):
                if BOOKS[i].get("title").casefold() == book_title.casefold():
                        BOOKS.pop(i)
                        break
                