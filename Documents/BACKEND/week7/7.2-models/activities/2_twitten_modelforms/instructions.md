As before, do one challenge at a time, and raise your hand if/when you
get stuck!


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
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Click around a little, until you understand the app.




Challenge 2: (With a partner)
-------------------

Discuss with a student next to you the following aspect of the Django
project:

* Examine microblog/models.py. Look at the new fields around the
  comments. Can you explain in your own words what these fields are
  doing, and why they are useful?

* Examine microblog/admin.py.  Create a superuser (python manage.py
  createsuperuser) and examine the admin interface. Try uploading an
  image to a tweet using the admin interface. See how the image appears
  in the feed? Can you find the template code that does this?





Challenge 3:
-------------------

Using the code in demos/modelform.py as a reference, replace the User
creation process with a ModelForm that does the same thing.

Hint #1: In the place of using "user = User.objects.create(...)", use the
following code:
    user = form.save()

That will create the user with the data specified.

Hint #2: Don't worry about the widget chosen for the password, for now.





Challenge 4:
-------------------

Replace the Tweet creation process with a ModelForm.

Hint: In the place of using form.save(), use the following code:
    tweet = form.save(commit=False)
    tweet.username = username
    tweet.save()

The commit=False allows us to make a change to the new Tweet we created
before we save it to the database.





Challenge 5:
-------------------

Using the code in demos/modelform.py as a reference, replace the User
profile editing process with a ModelForm that does the same thing.



Challenge 6:
-------------------

Using the code in demos/modelform.py as a reference, replace the Tweet
editing process with a ModelForm that does the same thing.


Challenge 7:
-------------------

Okay, time to enable tweets with image upload! You'll need to do 3 things:

1. Ensure the 'file' field is included in the ModelForm's field list.
This should be enough to show the file upload field when rendering the
form (although it won't work just yet).

2. Tell the browser to enable file uploads. This requires a change to
the <form> tag. This will require adding this special "enctype" property
to your form, as such:
    <form enctype="multipart/form-data" method="post" action=".">

3. When creating your tweet, do something like:
    TweetForm(request.POST, request.FILES)


Bonus Challenge:
-------------------

Look at settings.py, at the end. To get uploads working, we needed a
couple of tweaks. Can you broadly get what they are doing?


Advanced Challenge:
-------------------

Using a deployment method like Heroku will wipe your uploads every time you
push. This has to do with "12 Factor" apps, which is the ideal app set-up.
Thus, the uploads/ directory is only good for development. In real life, we
will want to use something called an "object store". The most popular object
store is Amazon S3.

1. Research 12factor app if you haven't already. https://12factor.net/

2. Research Amazon S3, and how to set it up with Django. Heroku has an
add-on that eases this process:
https://elements.heroku.com/addons/bucketeer

