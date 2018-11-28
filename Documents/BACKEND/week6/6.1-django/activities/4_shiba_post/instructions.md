As before, do one challenge at a time, and raise your hand if/when you
get stuck!


Challenge 1:
-------------------

1. Get this code running! This time feel free to reuse the previous
virtualenv shell.

2. Once you get it running, look at the templates. They've changed a bit.
Do you see the "extends" and "base.html"? Can you explain in your own
words what you think this does to the person next to you?

3. Do the thing you do with new projects: Add a print to every single
view, to better explore and understand the code.



Challenge 2:
-------------------

1. What happens if you add an adoption, and then hit refresh?
2. Try this a few times. Establish a correlation of what is happening.
3. Why is this happening, and how do you fix the duplicates?

Answer: The "GET" method allows refresh. This means that views that change or
add data will get re-run. It is not suitable for forms, or at least forms that
change or add data. The "POST" prevents refresh. It is better for forms.

4. Change the adoption page to use POST instead of GET. This will require a
change in both the template file, and a couple changes in the views.py file.

HINT: You will also need to add this code to your form:
    {% csrf_token %}
This adds security measures that Django requires to prevent forged POST
requests.




Challenge 3:
-------------------

Change the add a dog page to use POST instead of GET. This will require
a change in both the template file, and a couple changes in the views.py
file.



Challenge 4:
-------------------

Currently, its tedious to adopt dogs on a separate page. You should be
able just to click a button next to each dog. Implement this
functionality, so that there exists a button next to each dog that will
adopt that dog, without the need

HINT 1: Think about pre-filled in forms.
HINT 2: You can even make form elements hidden!





Challenge 5:
-------------------

Currently, a bug exists where there can be more than one dog with the
same ID number. Can you reproduce this bug? Can you fix this bug?

HINT: Consider generating a random number as the ID.



Bonus Challenge
-------------------

- Add a new feature to the adoption page: Have it say if the previous
  adoption attempt was successful or not



Extra Challenges
-------------------

*No solution provided for these since they interfere with previous challenges.*

- Google "include Django templatetag". Use it to share bits of HTML and
  templating between pages, and get the dogs list showing on the other pages,
  also.

- Look up "Django Forms". Can you write Django Form classes to replace all
  forms on this page?
