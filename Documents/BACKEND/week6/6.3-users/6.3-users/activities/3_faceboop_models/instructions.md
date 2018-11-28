As before, do one challenge at a time, and raise your hand if/when you
get stuck!


Challenge 1:
-------------------

1. As before, get the site running. Note how you cannot access the feed
unless logged in.

2. Run initial migrations:

    python manage.py migrate

3. Create a new Django Superuser (administrator account). Remember the
name / password you used. Clue:

    python manage.py createsuperuser

4. Log-in to the admin panel


Challenge 2:
-------------------

Background: So far, we have been using pre-made models. We are now going
to write our own custom model, this time for the WallPosts.

NOTE: This is a very tricky challenge to start with, so be sure to get
help when you get stuck.

Time to actually make the wall posts functional, and saving in the
database!  The syntax and structure is very similar to making a Form.
Examine the following clue:

    class ExampleModel(models.Model):
        single_line_field = models.CharField(max_length=30)
        multiple_line_field = models.TextField()

Using some modification of this example create a new model called
"WallPost" in wall/models.py.  Make sure the name of your two fields are
the same as the dictionary ("username" and "text" respectively).

Hint #1: Look at previous activities models.py as hints.



Challenge 3:
-------------------

Background: WHENEVER you create a new model or edit an existing model,
there are always two steps: 1. First, "create a migration" (migrations
consist of auto-generated code that update the database to support the
new data you are adding). 2. Then, "run the migration" to (this actually
executes or invokes the migration you created)

1. Run the following command to create the "migrations" necessary to
update your database to include your new model:

    python manage.py makemigrations

2. Observe how it reports back to you that it created a migration titled
something like "Create model WallPost".

3. Finally, re-run the "migrate" command to actually activate this
"migration", getting your database updated to the new model:

    python manage.py migrate



Challenge 4:
-------------------

Change the feed view to get the posts from the database. This is similar
to what we did in the previous activity with Users. A clue:

    from .models import WallPost
    posts = WallPost.objects.all()



Challenge 5:
-------------------

Change the feed view to save posts to the database.

Hint:

    WallPost.objects.create(
        username='example_user',
        text='example text',
    )





Bonus Challenge 1:
-------------------

Fix the search view to use WallPost objects instead of the posts list.
Replace "all" with filter.  Check out the following clue:

    WallPost.objects.filter(
        text__icontains="example search",
    )



Bonus Challenge 2:
-------------------

Can you follow the Django admin documentation to make it so that you can
add and edit posts in the database?
https://docs.djangoproject.com/en/2.0/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin



Bonus Challenge 3:
-------------------

Try adding a special __str__ method to the WallPost so it looks better
in the administrator interface, as such:

    def __str__(self):
        return '%s: %s' % (
            self.username,
            self.text,
        )

(Note: not included in solution, since it makes previous answers harder to
read. However, the clue should work as-is.)


Advanced Challenge:
-------------------

We'll get into ForeignKeys later, but this is a nice chance to use it
early. Can you replace "username" with a "user" field that is a
ForeignKey to the User model?
https://docs.djangoproject.com/en/2.0/ref/models/fields/#foreignkey

Once completed, can you create a user page that shows the posts for a
given user?


(Not completed in the solution, since conflicts with previous solutions)

