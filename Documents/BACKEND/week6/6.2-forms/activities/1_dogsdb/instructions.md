This is primarily a discussion activity. Work with the person next to
you to analyze and investigate the code. Only when you feel comfortable
with the existing code, go on to the Challenge 3 and beyond.

As before, do one challenge at a time, and raise your hand if/when you
get stuck!


Challenge 1:
-------------------

Get this code running. Refer to the steps from previous activities if
you get stuck.

Generally, it requires three steps:

    pipenv --python 3
    pipenv shell
    pipenv install django

Then finally:

    python manage.py runserver


Challenge 2:
-------------------

Discuss with your neighbor the following concepts:

1. What is the "app" and what is the "project"?

2. Look at how the template files relate to each other. Can you explain
how base.html works, and how the other template files relate to it?

3. Look at models.py. Models are what defines what columns are available
in our database. Open up the db.sqlite3 database file using the SQLite
DB Viewer. Do you see the correspondence?

4. Go to the "add dog page". Check the database file. Do you see the
correlation?

5. Remember: When you visit a URL that routes to (corresponds to) a view
function, it will invoke that view function running all code within it.
With this in mind, can you explain how visiting the "add dog page" adds
a dog?


Challenge 3:
-------------------

To get more used to both using models and views, write a new view that
is an alternate link, for adding a dog with the name "Bad Boye".

Hint #1: This requires adding a new view, which involves adding code in
urls.py AND views.py

Hint #2: Feel free to re-use the "add_dog" template.


Challenge 4:
-------------------

Now it's time to allow the user to select the name.

1. Create a new view for "custom dog". Keep it empty for now, except for
the "return render" bit. Add it to urls.py

2. Create a new template for "custom dog".

3. Add into the new template the following code:

    <form action="." method="POST">
        {% csrf_token %}
        <input name="dogname" placeholder="The Dog's Name" />
        <button>Submit</button>
    </form>

4. In the view function, add in the following code:

    print(request.POST)

From that, can you figure out how to finish this view so that you can
make custom dogs? (Hints after the blank below)













Hints:

    # First, check if they have submitted something:
    if 'dogname' in request.POST:

        # Then, get the name out of the POST dictionary
        name = request.POST['dogname']

        # Finally, actually create the appointment
        DogAppointment.objects.create(
            image_src="http://cdn.shibe.online/shibes/1fc9a53355b767a146fa7e6188c88ee557e77659.jpg",
            name=name,
            age=5,
            date="Tomorrow",
            time="Early in the morning",
        )


Bonus Challenge:
-------------------

Finish the dog adding page & view to allow customizing of all properties.

