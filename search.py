import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

def search_book(isbn,title,author):
    booklist={}
    book1=[]
    book2=[]
    book3=[]
    if isbn is not None and len(isbn) != 0:
        book1=db.execute(f"SELECT * FROM books WHERE isbn LIKE '%{isbn}%'")
    if title is not None and len(title) != 0:
        book2=db.execute(f"SELECT * FROM books WHERE title LIKE '%{title}%'")
    if author is not None and len(author) != 0:
        book3=db.execute(f"SELECT * FROM books WHERE author LIKE '%{author}%'")

    list=[]
    for i in book1:
        #print(i)
        list.append(i.title)
        list.append(i.author)
        list.append(i.year)
        booklist[i.isbn]=list
        list=[]

    list=[]
    for i in book2:
        #print(i)
        list.append(i.title)
        list.append(i.author)
        list.append(i.year)
        booklist[i.isbn]=list
        list=[]

    list=[]
    for i in book3:
        #print(i)
        list.append(i.title)
        list.append(i.author)
        list.append(i.year)
        booklist[i.isbn]=list
        list=[]
    #print(booklist)
    return booklist


#isbn=""  #take arguments from the function
#title="Van"
#author="Jo"


#if len(booklist) == 0:
    #print("No match found")
#else :
    #print(booklist)

if __name__=="search_book":
   search_book()
