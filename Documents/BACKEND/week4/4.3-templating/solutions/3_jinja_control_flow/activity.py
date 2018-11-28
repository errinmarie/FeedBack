# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# 1. As with the previous activity, create a new virtualenv using pipenv
# 2. Enter into that virtualenv
# 3. Install jinja2
# 4. Examine the following code. See if you can explain in your own words what
# every line is doing. Change it to say "Ready for Activity 3!"

from jinja2 import Template

template = Template('''
{% if is_ready %}
    Ready for Activity 3!
{% else %}
    Not ready for Activity 3...
{% endif %}
''')
result = template.render(
    is_ready=True,
)
print(result)




print('Challenge 2 -------------')
# Challenge 2:
# 1. Oh yay, another one of those "spot the mistakes" problems! This time, the
# only parts of this that are broken are in the Jinja template that is doing
# looping and if statements.
# 2. Uncomment the commented-out code and observe the errors that Jinja
# generates.
# 3. Fix everything. You will know it is fixed when it loops through all 5
# movies, printing their titles, summaries, and noting movies that are
# unusually long.

import json
movies = json.load(open('movies.json'))

template_string = '''
{% for movie in movies %}
    -------------------------------
    - {{ movie.title }}
    Facts:
        Title: {{ movie.title }}
        Summary: {{ movie.summary }}
    {% if movie.length > 150 %}
        Really Long: This movie is over 2.5 hours, yikes!
    {% endif %}
{% endfor %}
'''

movies_information_template = Template(template_string)
result = movies_information_template.render(
    movies=movies,
)
print(result)





print('Challenge 3 -------------')
# Challenge 3:
# Write the code for a new template and render it, such that it loops through
# all movies, printing out their title and runtime (labeled as minutes)

template_string = '''
{% for movie in movies %}
{{ movie.title }} | {{ movie.length }} min
{% endfor %}
'''
movies_information_template = Template(template_string)
result = movies_information_template.render(
    movies=movies,
)
print(result)






print('Challenge 4 -------------')
# Challenge 4:
# This is tough challenge!
# 1. Write a template that loops through all the baseball players found within
# the athletics.json file, outputting their name.
# 2. If the player joined after 2010, write "newer player" after their name.
# 3. Output "BOTH: Right" if they bat with their right hand AND throw with
# their right hand. Output "BOTH: Left" if the opposite. If is a mix of the
# two, then write: "Left, Bat - Right, Throw" (as an example)
# Hint: The data is "Bat": "R", and "Throw": "L"
players = json.load(open('athletics.json'))

template_string = '''
{% for player in athletes -%}
- {{ player.Name }}
    {%- if player['First Year'] > 2010 -%}
        |Newer Player
    {%- endif -%}
    |
    {%- if player.Bat == "R" and player.Throw == "R" -%}
        BOTH: Right
    {%- endif -%}
    {%- if player.Bat == "L" and player.Throw == "L" -%}
        BOTH: Left
    {%- endif -%}
    {%- if player.Bat == "L" and player.Throw == "R" -%}
        Bat: Left -- Throw: Right
    {%- endif -%}
    {%- if player.Bat == "R" and player.Throw == "L" -%}
        Bat: Right -- Throw: Left
    {%- endif %}
{% endfor %}
'''
athletics_template = Template(template_string)
result = athletics_template.render(
    athletes=players,
)
print(result)






print('-------------')
# Bonus Challenge
# Modify the above template to generate an HTML page containing a table,
# containing the same information. Save that HTML page to output.html

template_string = '''
<link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" type="text/css">

<body>
<table>
    <thead>
        <tr>
            <th>Rank</th> <th>Uniform</th> <th>Name</th> <th>Nationality</th>
            <th>Age</th> <th>Bat/Throw</th> <th>Height</th>
            <th>Weight</th> <th>Date of Birth</th> <th>First Year</th>
        </tr>
    </thead>
    <tbody>
        {% for player in athletes -%}
            <tr>
                <td>{{ player.Rank }}</td>
                <td>{{ player.Uniform }}</td>
                <td>{{ player.Name }}</td>
                <td>{{ player.Nationality }}</td>
                <td>{{ player.Age }}</td>
                <td>
                    {% if player.Bat == "R" and player.Throw == "R" %}
                        Right
                    {% endif %}
                    {% if player.Bat == "L" and player.Throw == "L" %}
                        Left
                    {% endif %}
                    {% if player.Bat == "L" and player.Throw == "R" %}
                        Bat: Left <br /> Throw: Right
                    {% endif %}
                    {% if player.Bat == "R" and player.Throw == "L" %}
                        Bat: Right <br /> Throw: Left
                    {% endif %}
                    {% if player.Bat == "S" %}
                        Bat: Switch
                    {% endif %}
                </td>
                <td>{{ player.Height }}</td>
                <td>{{ player.Weight }} lb</td>
                <td>{{ player['Date of Birth'] }}</td>
                <td>{{ player['First Year'] }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
</body>
'''
athletics_template = Template(template_string)
result = athletics_template.render(
    athletes=players,
)
open('output.html', 'w+').write(result)

