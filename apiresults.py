import os
from flask import jsonify
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

def apires(isbn):
    list=db.execute(f"SELECT rating FROM reviews WHERE isbn ='{isbn}'")
    count=db.execute(f"SELECT COUNT(*) FROM reviews WHERE isbn ='{isbn}'")
    if list == None:
        return jsonify({"error":"Invalid"}),422

    bookdetails=db.execute(f"SELECT title,author,year FROM books WHERE isbn ='{isbn}'")
    sum=0
    c=0
    for score in list:
        c=c+1
        sum=sum+score.rating

    avg_score=sum/c
    avg_score=round(avg_score,1)

    title=""
    author=""
    year=""
    for i in bookdetails:
        title=i.title
        author=i.author
        year=i.year

    return jsonify(
    title=title,
    author=author,
    year=year,
    isbn=isbn,
    review_count=c,
    average_score=avg_score
    )
