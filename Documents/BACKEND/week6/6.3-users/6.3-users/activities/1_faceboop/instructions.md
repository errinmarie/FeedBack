As before, do one challenge at a time, and raise your hand if/when you
get stuck.


Challenge 1:
-------------------

Get this code running. You should see a site that might coincidentally
resemble a popular social network when it is fully working. Refer to the
steps from previous activities if you get stuck.

Generally, it requires three steps:
pipenv --python 3
pipenv shell
pipenv install django

Then finally:
python manage.py runserver

Click around a little, until you understand the app. Note that the
posting and search functionalities are (intentionally) broken.




Challenge 2:
-------------------

Discuss with a student next to you the following aspects of the Django
project:

1. "faceboop" vs "wall", which is the Django project, which is the
Django app?

2. Examine faceboop/urls.py. Note the "name=" parameter. Now, examine
the "wall/templates/base.html", see the code {% url "home" %} and {% url
"feed" %}. Can you guess what it might be doing?

3. Can you figure out how the different navbar items highlight
conditionally based on what link you click on?



Challenge 3:
-------------------

- Note how the form to post share new content to the Faceboop feed isn't fully
  working.

- It's missing some code in the feed view (found in views.py). Fix it so that
  it shows the new data.


Challenge 4:
-------------------

Take a look at the NewFanPageForm. Flesh it out to include the following
fields:
* name
* date joined
* email

Hint: You might need to use an EmailField for email.  Look at previous
exercises, or demo code, for examples.


Challenge 5:
-------------------

Now, use this form you just created to add code to allow new Fan Pages to be
added to the homepage.



Advanced Bonus Challenge:
-------------------------

Presently, the "search" view is only a stub (that is to say, the
definition exists, but has no code).  Implement the search box
functionality. Create a new "search" template.  Write the necessary
functionality to only return posts that contain the search term entered.

* For full functionality, make it be case insensitive (see: `__icontains`, at
  https://docs.djangoproject.com/en/2.1/ref/models/querysets/ )

* To DRY out your template, add a template snippet and using include in
  both feed.html and search.html to include it

