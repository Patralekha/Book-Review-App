from flask import Flask,render_template,request
from flask_session import Session
from search import *
from book import *
from apiresults import apires
from userlogin import login,register
from usernamef import *
from flask import jsonify

app=Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
app.secret_key="473bv8"

session={}

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/signin/<string:sign>")
def signin(sign):
    return render_template("index2.html",sign=sign)

@app.route("/ulogin",methods=["GET","POST"])
def ulogin():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
        userid=login(email,password)
        if userid < 0:
            return render_template("incorrectinfo.html",text="You have entered wrong email or password!!")
        else:
            session["userid"]=userid
            name=fetchuser(userid)
            return render_template("layout2.html",res=False,booklist={},uid=session["userid"],name=name)


@app.route('/logout')
def logout():
    if "userid" in session:
        session.pop("userid",None)
        return render_template('index.html')
    else:
        text="User has already logged out"
        s=0
        return render_template("incorrectinfo.html",text=text,s=s)

@app.route("/uregister",methods=["GET","POST"])
def uregister():
    s=0
    if request.method == "POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        text=register(name,email,password)
        if text == 'Successfully registered!':
            s=1
        else:
            s=0
    return render_template("incorrectinfo.html",text=text,s=s)



@app.route("/search",methods=["GET","POST"])
def search():
    booklist={}
    res=False
    if "userid" in session:
        uid=session["userid"]
        if request.method == "POST":
            isbn=request.form.get("isbn")
            title=request.form.get("title")
            author=request.form.get("author")
            #print(isbn," ",title," ",author)
            booklist=search_book(isbn,title,author)
            #print(booklist)
            name=fetchuser(uid)
            if len(booklist) == 0:
                res=False
            else:
                res=True
            return render_template("layout2.html",res=res,booklist=booklist,name=name)
    else:
        return render_template("incorrectinfo.html",text="User not logged in!",s=0)



@app.route("/book/<string:isbn>/<string:title>/<string:author>")
def book(isbn,title,author):
    if "userid" in session:
        uid=session["userid"]
        user_reviews=review(isbn)
        noreview=True
        if len(user_reviews) == 0:
            noreview=True
        else:
            noreview=False

        grev=[]
        grev=goodreads_reviews(isbn)
        if len(grev) == 0:
            goodread=False
        else:
            goodread=True
        name=fetchuser(uid)
        value=api(uid,isbn)
        return render_template("layout3.html",isbn=isbn,title=title,author=author,goodread=goodread,grev=grev,noreview=noreview,user_reviews=user_reviews,uid=uid,value=value,name=name)
    else:
        return render_template("incorrectinfo.html",text="User not logged in!",s=0)


@app.route("/submitreview",methods=["GET","POST"])
def submitreview():
    if "userid" in session:
        uid=session["userid"]
        if request.method == "POST":
            comment=request.form.get("review")
            rating=request.form.get("rating")
            isbn=request.form.get("isbn")
            print(isbn," ",review," ",rating)
            submit_user_review(uid,isbn,rating,comment)
            name=fetchuser(uid)
    return render_template("layout2.html",res=False,booklist={},name=name)

@app.route("/api/<string:isbn>")
def bookapi(isbn):
    return apires(isbn)
