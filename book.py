import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

#takes arguments from the function takes the isbn number of the book and picks up reviews from the review table
def review(isbn):
    user_review=[]
    #isbn='0399153942'
    user_review=db.execute(f"SELECT * FROM reviews WHERE isbn ='{isbn}'")
    reviewlist=[]
    l=[]
    for i in user_review:
        uname=db.execute(f"SELECT username FROM users WHERE userid ={i.userid}")
        for j in uname:
            l.append(j.username)
        l.append(i.rating)
        l.append(i.review)
        reviewlist.append(l)
        l=[]
    return reviewlist


#fetch goodreads reviews using the api
def goodreads_reviews(isbn):
    KEY="dwBWavKfY1N2X5QgQpwGIw"
    res=requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": KEY, "isbns": isbn})
    list=[]
    if res.status_code!=200:
        print(res.status_code)
        #raise Exception("ERROR!")
    else:
        data=res.json()
        average_score=data['books'][0]['average_rating']
        ratings=data['books'][0]['work_ratings_count']
        list.append(average_score)
        list.append(ratings)
    return list

#submit a review to the review table if user can submit (using your api)
def api(userid,isbn):
    current_user_review=db.execute(f"SELECT rating,review FROM reviews WHERE userid='{userid}' AND isbn ='{isbn}'")
    uservals=[]
    for i in current_user_review:
        uservals.append(i.rating)
        uservals.append(i.review)

    if len(uservals) == 0:
        print("Please submit a review and rate the book before you go!")
        return True
        #take parameters from html page as rating and current_user_review
        #display submit review section on html page
    #    db.execute("INSERT INTO reviews(userid,isbn,rating,review) VALUES (:userid,:isbn,:rating,:review)",{"userid":userid,"isbn":isbn,"rating":rating,"review":review})
    else:
        #hide submit review section on html page
        print("You have already submitted a review for this book")
        return False

def submit_user_review(userid,isbn,rating,review):
    db.execute("INSERT INTO reviews(userid,isbn,rating,review) VALUES (:userid,:isbn,:rating,:review)",{"userid":userid,"isbn":isbn,"rating":rating,"review":review})
    db.commit()
