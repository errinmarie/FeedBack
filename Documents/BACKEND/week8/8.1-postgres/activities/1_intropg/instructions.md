Challenge 1:
--------------------------

For this first challenge, your goal is to install any necessary software
you need, then create a database on Heroku, and connect to it.

1. Installation (only need to do once)
    * Ubuntu Linux:
        sudo apt-get install postgresql-client
    * macOS:
        brew install postgres

2. Creating a new Heroku Postgres Database (need once per database):
    * Create a new Heroku app to play around with:
        heroku create
    * Provision for that app a new Postgres Database (free "hobby" tier):
        heroku addons:create heroku-postgresql:hobby-dev --app pure-crag-68

3. Connect to your database with the commandline client:
    heroku pg:psql --app pure-crag-68

NOTE: For the these last commands, you will need to change
"pure-crag-68" to the similarly random name your app got when you
created it.






Challenge 2:
--------------------------

For the second challenge, create the tables necessary to house the
following data. Add the data, and practice querying it.

General steps for working with Postgres:

    CREATE TABLE ... to create a table
    \d to check tables (it's your "ls")
    \d table_name to get more info on one table
    INSERT INTO ... to add data to a table
    SELECT * FROM table_name; to "see" the data in your table



|      | users         |
| ---- | ------------- |
| id   | username      |
|  1   |  janeqhacker  |
|  2   |  admin        |
|  3   |  dolanduck    |
|  4   |  dril         |


|      | tweets   |                    |
| ---- | -------- | ------------------ |
| id   | user_id  | text               |
|  1   |  1       |  h4ck th3 pl4n37   |
|  2   |  3       |  hi i'm dolan      |
|  3   |  4       |  no                |
|  4   |  3       |  gooby pls         |



HINT #1: Look at your cheatsheet to remember SQL syntax.

HINT #2: Remember to end all your SQL statements with ";"! Otherwise it
will think you are still adding on to the same statement and come up
with a syntax error.



Challenge 3:
--------------------------

Rinse and repeat, now with even more data.


|      | users         |
| ----:|---------------|
| id   | username      |
|  1   |  morticia     |
|  2   |  gomez        |
|  3   |  unc_fester   |
|  4   |  wednesday    |


|      | photos   |                    |
| ----:|---------:|--------------------|
| id   | user_id  | photo              |
|  1   |  1       |  /ph/fa29aec3.jpg  |
|  2   |  3       |  /ph/3aec49ef.jpg  |
|  3   |  4       |  /ph/63dd3fc0.jpg  |
|  4   |  3       |  /ph/b3759be4.jpg  |


|      | tags       |            |
| ----:|-----------:| ---------- |
| id   | photo_id   | text       |
|  1   |  1         |  nofilter  |
|  2   |  1         |  deadtome  |
|  3   |  3         |  nofilter  |




Challenge 4:
--------------------------

Using these tables, practice each of the following SQL features:

    ALTER TABLE
    DROP TABLE
    CREATE INDEX



Advanced Challenges:
--------------------------

- Using these tables, look up Postgres feature we haven't covered yet
  (such as JSON data in database) and practice these.

- If you have time, look up online tutorials on installing and running
  postgres locally (as opposed to Heroku). This is something you may
  need to do at some point in the future, so doesn't hurt playing around
  with that now. It isn't too hard, though sometimes can have hang-ups.
