As before, do one challenge at a time, and raise your hand if/when you get
stuck!


Challenge 1:
-------------------

Get this code running. You should see a site that might coincidentally resemble
a popular social network when it is fully working. Refer to the steps from
previous activities if you get stuck.

Generally, it requires three steps:
pipenv --python 3
pipenv shell
pipenv install django

Then finally:
python manage.py migrate
python manage.py runserver

Click around a little, until you understand the app. Note that the login
functionality is (intentionally) broken.




Challenge 2:
-------------------

You will be building the wall-posting mechanic of this application, so
that you can create posts on user's walls, and each user has a separate
wall. Your goal now is to implement the "C" aspect of CRUD. Look at the
views.py for further clues.


Challenge 3:
-------------------

- Implement the "R" aspect of CRUD.


Challenge 4:
-------------------

- Implement the "D" aspect of CRUD.


Challenge 5:
-------------------

- Implement the "U" aspect of CRUD.

