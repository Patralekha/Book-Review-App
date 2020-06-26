import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))


def fetchuser(uid):
    r=db.execute(f"SELECT username FROM users WHERE userid ={uid}")
    name=''
    for i in r:
        name= i.username
    return name


#user_review=[]
#isbn='0399153942'
#fetch user reviews from review table (your api)
#user_review=db.execute(f"SELECT * FROM reviews WHERE isbn ='{isbn}'")
#reviewlist=[]
#l=[]
#for i in user_review:
#    uname=db.execute(f"SELECT username FROM users WHERE userid ={i.userid}")
#    for j in uname:
#        l.append(j.username)
#    l.append(i.rating)
#    l.append(i.review)
#    reviewlist.append(l)
#    l=[]
#print(reviewlist)
