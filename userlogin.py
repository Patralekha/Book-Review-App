import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine=create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))


def login(email,password):
    userid=db.execute(f"SELECT userid FROM users WHERE emailid ='{email}' AND password='{password}'")
    if userid == None:
        return -1
    else:
        id=-999
        for i in userid:
            id=i.userid
        return id


def register(username,emailid,password1):
    email=db.execute(f"SELECT emailid FROM users WHERE emailid ='{emailid}'")
    password=db.execute(f"SELECT password FROM users WHERE password ='{password1}'")
    password_verify=''
    email_verify=''

    for i in password:
        password_verify=i.password
    for i in email:
        email_verify=i.emailid
    #print(email_verify," ",password_verify)

    if email_verify == '' and password_verify == '':
        db.execute("INSERT INTO users (username,password,emailid) VALUES (:username,:password,:emailid)",{
        "username":username,"password":password1,"emailid":emailid})
        db.commit()
        return "Successfully registered!"
    else:
        if email_verify != '' and password_verify != '':
            return "Choose another email and password"
        elif email_verify != '':
            return "Choose a different email id.A user with this emailid already exists!!"
        elif password_verify != '':
            return "Password not available!Choose a different password!"
