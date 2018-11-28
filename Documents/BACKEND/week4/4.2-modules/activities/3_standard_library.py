# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# 1. Examine the following sample code. It uses the pprint module to
# "pretty print" a Hello World message.
# 2. Create a list of dictionaries and put it in a variable. It doesn't
# have to have meaningful data, it can be nonsense. For time's sake,
# consider just using the code you wrote for Homework 3. 
# 3. Use pprint to print the list of dictionaries.
# 4. Look up online how to use pprint to indent the output with 2
# spaces, and a width of 30 characters.




pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Me",
    },
    {
        "filename": "content/stories.html",
        "output": "docs/stories.html",
        "title": "Stories",
    },
]

import pprint
pprint.pprint('Hello world')
pprint.pprint(pages)

print('Challenge 2 -------------')
# Challenge 2:
# Import syntax challenge! Once again, we have some commented code that
# has a variety of syntax errors. Go through each line and fix the
# syntax typo.

import time
import subprocess
import datetime
import random
print(random.randint(5, 10))
data = ['a', 'b', 'c']
random.shuffle(data)
print(data)




print('Challenge 3 -------------')
# Challenge 3:
# 
# 1. Examine the "example_json.json" file adjacent to this one. What do
# you see? JSON is a file format that is almost identical to Python
# dictionaries.
# 2. Uncomment the following code. Examine it. Add the missing import
# statement to get it working.
# 3. Can you combine it with Python code that reads in the JSON file
# into a string, so that it reads JSON code from a file?

import json
example_json = open('example_json.json').read()
d = json.loads(example_json)
print(d['a'])





print('Challenge 4 -------------')
# Challenge 4:
# 1. Look up the 'sys' module, and print out the value of 'sys.argv'
# 2. What type of data is this?
# 3. Can you get extra values to be displayed when printing out
# sys.argv? Hint: When executing the Python program, see what happens
# when you add stuff AFTER the filename of the Python program.
# 4. Can you modify your code to print out ONLY the extra values,
# skipping the stuff that stays the same at the beginning? Hint: Use
# "list slicing" syntax





print('Challenge 5 -------------')
# Challenge 5:
# 1. Uncomment the two following lines of code.
# 2. Add the missing code to get them working.
# 3. What do they do? What are the differences between them?

subprocess.run('ls')
output = subprocess.check_output('ls')




print('Challenge 6 -------------')
# Challenge 6:
# Using the code from Challenge 5, plus the string method "split" and a
# for-loop, go through all the files in the current directory, printing the
# name of each one on a separate line.

# Can you figure out how to get rid of the "b"? (You'll know when you see it ;)





print('------------')
# Bonus Challenge:
# Install the "figlet" application on your Linux package manager or
# Homebrew for macOS.  Write a stand-alone Python script that uses
# "time" to delay displaying a "Time's Up!" message in a large font.
# Combine it with sys.argv it to make it a useful commandline timer.



