import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
        <a href="/new-page">Challenge 3 - create a new page </a> <br />
    ''')


def about_me(request):
    # Django comes with a "shortcut" function called "render", that lets us
    # read in HTML template files in separate directories to keep our code
    # better organized.

    # The template files all go in the "templates" directory, just like we have
    # been doing in homework.

    # The template render context is in a separate dictionary that is passed to
    # the "render" function, as such.
    context = {
        'name': 'Misty',
        'pokemon': 'Psyduck',
    }
    return render(request, 'about_me.html', context)


def github_api_example(request):
    # We can also combine Django with APIs, or 
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)



def another_page(request):
    context = {
    }
    return render(request, 'another_page.html', context)

