CREATE TABLE books(
isbn VARCHAR PRIMARY KEY,
title VARCHAR NOT NULL,
author VARCHAR NOT NULL,
year DATE NOT NULL
);


CREATE TABLE users(
  userid SERIAL PRIMARY KEY,
  username VARCHAR NOT NULL,
  password VARCHAR NOT NULL,
  emailid VARCHAR NOT NULL
);

CREATE TABLE reviews(
  id SERIAL PRIMARY KEY,
  userid INTEGER REFERENCES users(userid),
  isbn VARCHAR REFERENCES books(isbn),
  rating FLOAT ,
  review VARCHAR
);
