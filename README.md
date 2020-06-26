# Book-Review-App
A book review application built using Python,Flask,PostgreSQL,HTML,CSS,Bootstrap,Goodreads API that allows readers to search for books and reviews and ratings that any book has received and leave their own reviews.This App also has an API usage feature where it can be used to get average score and rating given to a book by users of this app.

Python files
application.py:Flask application that links functions with the html pages.Also runs functions from various other python files.

userlogin.py:1)contains login function that validates email and password entered.If validation is successful it returns userid.
             2)contains register function that accepts name,email,password ,validates them and returns a success message or a failure message       accordingly.


usernamef.py:1)contains fetchuser function that is used to fetch username from given userid.

search.py:1)contains search_book function that accepts isbn,title,author(any or all of the fields can be empty),generates matching results and returns the matching results as a dictionary 'booklist' with isbn as key and title,author,year as list values.

book.py:1)review function:fetches scores and ratings left by users of our app(if any)
        2)goodreads_reviews function:fetches average score and rating of the book from goodreads using goodreads api
        3)api function:checks if current user has already submittesd review of this book
        4)submit_user_review function:accepts review and score submitted by a user and inserts data into 'reviews' table

apiresults.py:1)apires function: when users make a GET request to  website 127.0.0.1/api/<isbn> route, where <isbn> is an ISBN number, this function  returns a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score.


import.py:reads books.csv and inserts each line into books table

create.sql:contains sql statements to create the table books,users and reviews

templates(HTML pages)
index.html:Cover page
           The first page of the app.Tells users about the app and provides users options to login(for existing users) or register(if new).

index2.html:Registration and login page
            Contains form for registration(for new users) and login form(for existing users)

layout2.html:Search page
             Allows a user to search for a book by its isbn,title or author.Partial inputs also generate results if they match.Matching results are displayed on the page if there are any.Also includes information on how to get API results for a book.

layout3.html:Book page
             Displays Goodreads reviews of the selected book from matching results,reviews left by any user and a form to leave review and score if the user has not submitted any review before.

incorrectinfo.html:A standard layout page that displays warning when any wrong information is entered in any of the forms or when any validation fails or when user is not logged in.Also displays success message when new user registration is successful.
