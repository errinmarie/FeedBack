As before:
- Most of this activity is working on code understanding
- One challenge at a time
- Raise your hand if/when you get stuck
- Use print statements to debug - early and often


Challenge 1:
-------------------

Get this code running. You should see a site that might coincidentally
resemble a popular microblogging service when it is fully working. Refer
to the steps from previous activities if you get stuck.

Generally, it requires three steps:
pipenv --python 3
pipenv shell
pipenv install django

Then finally:
python manage.py migrate
python manage.py runserver

Click around a little, until you understand the app. The app should be
functioning as-is, but missing certain functionality: Notably, deleting
and editing posts.



Challenge 2: (With a partner)
-------------------

Discuss with a student next to you the following aspect of the Django project:

- Examine microblog/admin.py.  Create a superuser (python manage.py
  createsuperuser) and examine the admin interface. See how Tweet (a
  custom model) appears in the admin interface? Play around with
  creating and deleting tweets. Custom models do not appear by default,
  but instead a line of code has to be added. With the other student,
  figure out which file was changed to make an app appear in the admin
  interface (Hint: this file is very logically named, and in microblog).

- Examine microblog/models.py.  Do you see the __str__ method of the
  Tweet class? Does the text or structure look familiar to something you
  just saw? What do you think it is doing? Try modifying it (slightly,
  e.g. only change "said" to "tweeted") and see if you can confirm what
  it is doing.

- Look at lines 92-102 of microblog/views.py. This performs the "R" in
  CRUD, and set up the context for rendering the template. Can you
  explain what each line is doing?




Challenge 3: (With a partner)
-------------------

Discuss with a student next to you the following aspect of the Django
project:

- Compare twitten/urls.py and microblog/views.py. Can you figure out how to use
  your browser to delete a tweet? (No code changes are necessary! To accomplish
  this, you need to type a URL in the browser's navigation bar to cause it it
  to happen.)

- Examine the `microblog/templates/pages/all_pages.html` and the
  `microblog/templates/pages/user_page.html` files. Can you explain what the
  "include" template-tag is doing? Why do you think we have a "snippets"
  directory? (Hint: Neither of these are a trick questions, it's doing exactly
  what you might guess.)




Challenge 4:
-------------------

Ever said something you wish you hadn't? Time to add a delete feature.  Use the
research you did in Challenge 3 to figure out how to add a link to every tweet
that will delete that tweet.

- HINT #1: You should accomplish this ONLY by editing a template.
- HINT #2: You can access the tweet's ID by using {{ tweet.id }}

Challenge 5:
-------------------

Now, make sure the delete link only appears on tweets that you tweeted.
E.g. you shouldn't be presented a link to delete other people's links.

- HINT #1: You should accomplish this ONLY by editing a template.
- HINT #2: You can access the currently logged in user with "user" (this is
  built-in to Django)
- HINT #3: Use an if statement, you can do something like like:
    {% if user.username == "dril" %}
    {% endif %}
- Hint #4: You will have to change the "dril" to something else. Look at the
  surrounding code for a clue.


Challenge 6:
-------------------

Currently, the edit profile link appears on every page. Make it only
appear on the page of the user who is logged in.

HINT #1: You should accomplish this ONLY by editing a template.
HINT #2: You can access the currently logged in user with "user" (this
is built-in to Django), and you can access the user of the profile you
are viewing with "user_on_page" (this is not built-in to Django, but
rather specified in this particular app's views, see the user_page view
in views.py).





Bonus Challenge #1:
-------------------

Implement an "Edit Tweet" feature. This one requires a lot more
template-fu!

HINT: You should accomplish this ONLY by editing a template.


Bonus Challenge #2:
-------------------

Look up Bootstrap modals. Make your "Tweet Editor" appear in a modal for
a smooth UX.

HINT: You should accomplish this ONLY by editing a template.


Advanced Challenge:
-------------------

If you followed the instructions (and only edited the template), this
application has A LOT of security holes. What are they? How would you
fix them?


