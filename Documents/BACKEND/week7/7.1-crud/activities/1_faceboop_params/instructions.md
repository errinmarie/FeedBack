As before, do one challenge at a time, and raise your hand if/when you
get stuck!


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
python manage.py migrate
python manage.py runserver

Click around a little, until you understand the app. Note that the login
functionality is (intentionally) broken.




Challenge 2:
-------------------

Discuss with a student next to you the following aspect of the Django
project:

* Examine faceboop/urls.py. Note <username> in brackets. Now, look at
  the views.py. Can you explain how the username parameter of the
  `user_feed` view relates to the <username> of the urls.py path?
  Experiment with typing different URLs in the browser. Can you
  establish corresponding behavior?


* Examine the commented code in `user_feed`. Can you explain what it will
  do when you uncomment it?



Challenge 3:
-------------------

- Uncomment the code provided in the `user_feed` view. Examine the feed.html
  template.

- By ONLY changing code in the `user_feed` view, can you make the template
  display the expected information about the user?  (That is, `first_name`,
  `last_name`, and `email`.)


Challenge 4:
-------------------

Take a look at the `view_city` view. Take a look at the urls.py. Follow
the same pattern established in the previous view to get the city view
showing in the template.

Your goal is to get it to say:

    The Great City of "Oakland"

if you visit /city/Oakland/

NOTE: There is no City model or anything like that. Don't over-think this. Our
initial goal is to just get it to say the above message at that URL.


Challenge 5:
-------------------

Context: The URL parameters can be of a couple different types. By default, if
there is no ":" between the <> brackets, it is a string type of any combination
of characters (including spaces). There are two other notable types, "int" and
"slug". "Int" is for integer numbers, and "slug" is just like the default,
except it ensures dash-separated-strings-like-this, which is good for article
titles (called "slugs" in the publishing business).

Research the different types here:
https://docs.djangoproject.com/en/2.0/topics/http/urls/#captured-parameters

* `<slug:article_name>`   -- this is for a "slug" type
* `<int:id_number>`       -- for an integer in a URL

* Using this knowledge, make an new URL and view, that accepts the ID number of
  a user, instead of the username, but otherwise behaves the same as the view
  we dealt with previously.


Challenge 6:
-------------------

Work on the city page template. Can you add code to make the title of the web
browsing tab be "Oakland - Faceboop Cities" (with Oakland being replaced by the
city page you are looking at?).



Bonus Challenge 1:
-------------------

For DRYer code, its possible for the same view to have multiple URL routes, and
for views to have defaults. Make it so that the username is optional for the
username URL, and defaults to the username of the logged-in user.


Bonus Challenge 2:
-------------------

Log-in system. Django has pre-written views for handling logging in. This will
involve the following steps:

1. Add in the pre-written views to your URLs.py. Add the following line:

    # Add this at the top
    from django.urls import path, include

    # ... and add the following within your urlpatterns:
    path('accounts/', include('django.contrib.auth.urls')),

2. Add in a setting to redirect successful log-ins to the homepage. This goes
at the bottom of your settings.py:

    LOGIN_REDIRECT_URL = '/'

3. Fix the form on the homepage to point to "accounts/login/" with its action.
This can either look like:

    <form action="/accounts/login/" method="POST">

    Or, using "named" views, you can write simply:

    <form action="{% url 'login' %}" method="POST">

4. Try it out! You should have a successful log-in system.



This will work now for most situations, but many situations will fall-back on
Django's default, ugly look.  To style different situations with custom
templates, check out the following tutorial:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

You'll need to include your own template. You need to put this in a directory within your
templates directory, as such:

    registration/login.html

(This is the page done in the solution)

