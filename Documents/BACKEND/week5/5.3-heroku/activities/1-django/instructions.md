In this activity we want to warm up our Django skills and make a simple
website.


Challenge 1
-----------

Get the code working!
1. Run "pipenv --python 3" to create a new virtualenv
2. Run "pipenv shell" to enter the virtualenv
3. Run "pipenv install" to install dependencies that are written in the
Pipfile (in this case, only Django)
4. Run python manage.py runserver to run the Django Python server itself
5. Now, visit localhost:8000 or 127.0.0.1:8000 (both will do the same thing).
6. What's the first thing you do with a new Python file? Add a print! Add a
print to the index function, just about the return statement.

Challenge 2
-----------

- Did you notice that there is an "About me" link that goes to a 404 page?
  There is something wrong with the code.
- Spot the mistakes and fix the code by modifying the manage.py file (but
  don't touch the boilerplate at the bottom!).


Challenge 3
-----------

- Add a brand new page called "contact"
- For now, just have it say "Contact me!"
- Make sure there is a link from the homepage to this page, and also a link
  back to the homepage
- Hint: You will have to add code in multiple spots!


Challenge 4
-----------

- Update your Contact page to include the following HTML form code:

    <form method="POST" action="/contact">
        <input name="myname" placeholder="Your name" />
        <input name="message" placeholder="Your message" />
        <button>Submit</button>
    </form>

- In the function defined for your contact page,
  try adding the following print code before the
  return statement:

    message = request.POST.get('message')
    print('Message received:', message)

- Can you figure out a cause-and-effect with request.POST and messages
  being received?

- Add additional code to also print out the name, if any.


Challenge 5
-----------

- Add in code that will put the message and name into a dictionary that is
  appended to a list

- The list should be "global" in scope (e.g. outside of any function)

- Hint: You should only add it if they do indeed submit something!


Challenge 6
-----------

- Now, add in code that generates an HTML list containing the messages that
  people leave.

- Hint:
    messages_html = '<ol>'
    for message in messages:
        messages_html += '<li>' + message['name'] + ': ' + message['message'] + '</li>'


Bonus Challenge
---------------

- Create a "chat room" where you first enter a username, and then can enter
  a message.

- What are limitations of your chat room?

