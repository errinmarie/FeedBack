from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context


def index(request):
    return HttpResponse('''
        <h1>Welcome to my homepage</h1>
        <a href="/my-favorite-characters">My favorite Game of Thrones characters</a> <br />
        <a href="/about-me">About me</a> <br />
        <a href="/contact">Contact</a> <br />
        <a href="/chat">Chat room</a> <br />
    ''')


def characters(request):
    return HttpResponse('''
        <h1>My favorite Game of Thrones Characters</h1>
        <ul>
            <li>Daenerys Targaryen</li>
            <li>Jon Snow</li>
            <li>Tyrion Lannister</li>
            <li>Arya Stark</li>
        </ul>
        <hr />
        <a href="/">Back to home page</a>
    ''')


def about_me(request):
    return HttpResponse('''
        <h1>About me</h1>
        <p>Just your average django dev</p>
        <hr />
        <a href="/">Back to home page</a>
    ''')

messages = [] # Challenge 5

def contact(request):

    # Challenge 4
    message = request.POST.get('message')
    print('Message received:', message)

    name = request.POST.get('myname')
    print('Name received:', name)

    # Challenge 5
    if name and message:
        message_dict = {
            'message': message,
            'name': name,
        }
        messages.append(message_dict)

    # Challenge 6
    messages_html = '<ol>'
    for message in messages:
        messages_html += '<li>' + message['name'] + ': ' + message['message'] + '</li>'
    messages_html += '</ol>'

    return HttpResponse('''
        <h1>Contact me!</h1>
        <p>Tell me your thoughts</p>

    ''' + messages_html + '''

        <form method="POST" action="/contact">
            <input name="myname" placeholder="Your name" />
            <input name="message" placeholder="Your message" />
            <button>Submit</button>
        </form>

        <hr />
        <a href="/">Back to home page</a>
    ''')


## BONUS below
chat_messages = []

def chat(request):

    # Check if they have entered a username. IF they haven't, display the "log
    # into the chatroom" screen.
    username = request.GET.get('username')
    if not username:
        # Not logged in, allow user to log in
        return HttpResponse('''
            <h1>Chat</h1>
            <form method="GET" action="/chat">
                <input name="username" placeholder="Enter your username" />
                <button>Log-in</button>
            </form>
            <hr />
            <a href="/">Back to home page</a>
        ''')

    message = request.POST.get('message')
    if message:
        message_dict = {
            'message': message,
            'username': username,
        }
        chat_messages.append(message_dict)

    # Challenge 6
    messages_html = '<ol>'
    for message in chat_messages:
        messages_html += '<li>' + message['name'] + ': ' + message['message'] + '</li>'
    messages_html += '</ol>'

    return HttpResponse('''
        <h1>Chat</h1>

    ''' + messages_html + '''

        <form method="POST" action="/chat">
            <input name="message" placeholder="Your message" />
            <button>Submit</button>
        </form>

        <hr />
        <a href="/">Back to home page</a>
    ''')


urlpatterns = [
    path('', index),
    path('my-favorite-characters', characters),
    # Challenge 2: v-- Fix this
    path('about-me', about_me),
    # Challenge 3 - Make new page
    path('contact', contact),
    # Bonus
    path('chat', chat),
]


# Boilerplate -- Don't worry about understanding anything from here down
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=sys.modules[__name__],
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
