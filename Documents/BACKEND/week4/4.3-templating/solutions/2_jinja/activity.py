# REMINDER: Only do one challenge at a time! Save and test after every one.

from jinja2 import Template

print('Challenge 1 -------------')
# Challenge 1:
# Examine the following code. See if you can explain what every line is
# doing. Change the name to your name.

template = Template('Hello, {{ name }}!')
result = template.render(name='Joan')
print(result)


print('Challenge 2 -------------')
# Challenge 2:
# Write the code to utilize this template to render your own name,
# favorite color, favorite food, and favorite book.


user_information_template = Template('''
<p>Name: {{ name }}</p>
<p>Favorite color: {{ color }}</p>
<p>Favorite food: {{ food }}</p>
<p>Favorite book: {{ book }}</p>
''')

result = user_information_template.render(
    name='Samwise Gamgee',
    color='Green',
    food='Taters',
    book='There and Back Again',
)
print(result)



print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the print function invocation. Only modify the template code
# to add the template variables necessary to categorize the foods. The
# first done is done for you.

template_code = '''
Healthy foods: {{ foods.fruit }}, {{ foods.vegetable }}, {{ foods.cold_dish }}
Junk foods: {{ foods.snack }}, {{ foods.drink }}, {{ foods.sandwich }}
'''

food_template = Template(template_code)
foods = {
    'fruit': 'apple',
    'vegetable': 'carrot',
    'sandwich': 'burger',
    'drink': 'mtn dew',
    'cold_dish': 'salad',
    'snack': 'doritos',
}
print(food_template.render(foods=foods))






print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the print function invocation. Only modifying the "context"
# dictionary, can you make this print the HTML of a simple website?


template_code = '''
<h1>{{ title }}</h1>
<p>My blog posts:</p>
<h2>{{ blog_post_titles|first|title }}</h2>
<p>{{ blog_posts|first|truncate }}</p>
'''
context = {
    'title': 'Thoughts by Samwise Gamgee',
    'blog_post_titles': ['my journey in middle earth'],
    'blog_posts': ['''As "punishment" for eavesdropping on Gandalf's
    conversation with Frodo regarding the One Ring, I was made Frodo's
    first companion on his journey to Rivendell. They we were joined by
    Meriadoc Brandybuck and Peregrin Took, Frodo's cousins, and
    journeyed together to Rivendell, where the Council of Elrond took
    place and I joined the Fellowship of the Ring.'''],
}

print(Template(template_code).render(context))



print('Challenge 5 -------------')
# Challenge 5:
# Uncomment the print function invocation. Only modify the template code
# adding filters necessary to do the thing it says.  You'll have to
# research different filters here:
# http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters


template_code = '''
All noodles: {{ noodles|join(', ') }}
Alphabetical: {{ noodles|sort|join(', ') }}
Reverse alphabetical: {{ noodles|sort|reverse|join(', ') }}
First: {{ noodles|first }}
Last, with a capital letter: {{ noodles|last|title }}
First alphabetically: {{ noodles|sort|first }}
Last alphabetically: {{ noodles|sort|last }}
Number of different types of noodles: {{ noodles|length }}
'''

noodles = [
    'soba',
    'ramen',
    'lo mein',
    'spaghetti',
    'jap chae',
    'vermicelli',
    'gnocchi',
]

print(Template(template_code).render(noodles=noodles))





# Bonus Challenge
template_code = open('madlib.html').read()
new_template = Template(template_code)
new_html = new_template.render(
    name=input('Your name? '),
    adjective=input('An adjective?'),
    event=input('An event in your life? '),
    celebrity1=input('Name a celebrity: '),
    celebrity2=input('Name another celebrity: '),
    noun1=input('A noun? '),
    noun2=input('And another noun? '),
    noun3=input('And a plural noun? '),
    verb1=input('A verb? '),
    verb2=input('Another verb? '),
    verb3=input('And a final verb?'),
)
open('madlib_output.html', 'w+').write(new_html)



