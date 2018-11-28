As before, do one challenge at a time, and raise your hand if/when you
get stuck!


Challenge 1:
-------------------

Get this code running.  Refer to the steps from previous activities if
you get stuck. It's okay to re-use a virtualenv that you created from a
previous environment, if you want (e.g., if you are already "in" the
virtualenv, as indicated by the parenthesis before your prompt)

Generally, it requires three steps:
pipenv --python 3
pipenv shell
pipenv install django

Then finally:
python manage.py runserver


Challenge 2:
-------------------

Experiment with creating dog appointments and sitters. Examine how all
the code is working together. Discuss with your neighbor the following
concepts:

1. Look at how the template files relate to each other. Can you explain how
base.html works, and how the other template files relate to it?

2. Can you explain how the forms send POST requests to the server?

3. How is data added to the database? How can you use DBViewer to see
the data getting added?


Challenge 3:
-------------------

Time to get to work! Presently, when adding a sitter, you are only
getting their first name. We want to be able to add other attributes to
the sitter, also.

1. Examine the code in views.py, and the code in models.py. Can you
determine which fields are missing?

2. Follow the same pattern you see in views.py and add_sitter.html to
add support for the missing fields.

Hint: This requires adding code in views.py and add_sitter.html


Challenge 4:
-------------------

- See how you can enter in "garbage data" for the phone-number and email
  for the sitter, and time and date for the dog appointment?

- Checking the validity of data entered by users is called "form
  validation".

- Write in pseudocode how you might validate this data entered by the
  user.

#SPECIFY THE TYPE, LIKE INTEGER, STRING, DATE FORMAT, ETC.
#IF FORMAT DOES NOT EQUAL THE SPECIFIED TYPE, SEND BACK AN ERROR MESSAGE.

- This functionality should also report back to the user when they
  entered something incorrect in these fields, giving them a chance to
  fix it. (e.g. You entered an incorrect email! It should have an "@"
  symbol.)

NOTE: You can also do this at the "models" level, but let's not think
about that for now.


Challenge 5:
-------------------

Dog age is the HTML input type of "number". This prevents the user from
entering a non-number in the form. Can you figure out a way to "hack"
this protection, and send invalid ages to the backend?


Challenge 6:
-------------------

Implement the code for Challenge 4. This will require both Python and template
changes (to report back to the user when something went wrong).


Advanced Challenge:
-------------------

How might you write the code to allow "booking" of the dog sitting
appointments? This feature should exist as a button on each dog (each
dog representing thus one appointment timeslot). When clicked, it takes
the user to a new page, that lets them select which sitter booked for
this dog. Forget about saving this data to the database for now, just
write everything except for this.

Write the pseudocode for this feature. If you have time, implement this
feature.

