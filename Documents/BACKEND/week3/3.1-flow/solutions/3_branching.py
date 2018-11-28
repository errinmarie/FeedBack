print('------------- Challenge 1')
# Challenge 1:
# Remember this? After line 11, each portion of code has one or more typos.
# Uncomment the following lines of code and fix the typos and mistakes as you
# go along.

name = "Brock"
if name == "Brock":
    print("Hi Brock!")
else:
    print("I don't know who you are.")

name = "Gary"
if name == "Brock":
    print("Hi Brock!")
else:
    print("I don't know who you are.")

age = 22
if age > 21:
    print("Old enough to drink")
else:
    print("Too young to drink")

age = 17
if age > 21:
    print("Old enough to drink")
else:
    print("Too young to drink")


print('------------- Challenge 2')
# Challenge 2:
# Okay, get the idea of the if statement? Now its time to get more practice.
# For each of the following variables, examine the comment, and write code
# using if/else that conditionally prints "yes" or "no" if the condition
# described by the comment is met.

person_a = 'johann'    # is person_a equal to 'samantha'?
if person_a == 'samantha':
    print("yes")
else:
    print("no")


person_b = 'samantha'  # is person_b equal to 'samantha'?
if person_b == 'samantha':
    print("yes")
else:
    print("no")


x = 100  # is x greater than 50?
if x > 50:
    print("yes")
else:
    print("no")


y = 13   # is y equal 50?
if y > 50:
    print("yes")
else:
    print("no")






print('------------- Challenge 3')
# Challenge 3:
# Look at your Python Week 3 cheatsheet. Examine the syntax and behavior of the
# following concepts: "elif", "pass", "and", "or"
# 
# Create variables and experiment with writing if statements that demonstrate
# all employ all of these features. The end result will look like Challenge 2,
# but it is up to you what you want to name your variables and which conditions
# you want to check for.

name = 'Ash'
pokemon = 'Pikachu'

if name == 'Ash' and pokemon == 'Pikachu':
    print("It's Ash with a Pikachu!")

name = 'Misty'
if name == 'Ash' or pokemon == 'Pikachu':
    print("Either Ash or Pikachu is here...")

if name == 'Ash':
    pass
elif name == 'Misty':
    print('Misty is here.')
else:
    pass





print('-------------')
# Bonus Challenge 1:
# Try uncommenting the following code. Can rewrite the if statements from the
# top to depend on user input?
name = input('Name? ')
age_string = input('Age? ')
age = int(age_string)

if name == "Brock":
    print("Hi Brock!")
else:
    print("I don't know who you are.")
if age > 21:
    print("Old enough to drink")
else:
    print("Too young to drink")





# Bonus Challenge 2:
# Copy the "locations" structure from the previous activity's solution here.
# Can you use "inputs" to ask the user for information on another location and
# add it to the list?

# One very simple way to do it:
locations = [
    {
        'name': input('Location name? '),
        'latitude': input('Latitude? '),
        'longitude': input('Longitude? '),
        'review': [
            input('Review? '),
        ],
    },
]

print("Okay here's the locations array:")
print(locations)

# A cleaner, more "Pythonic" way might be to first put in variables. This also
# stores lat and long as a float:
# name = input('Location name? ')
# latitude = float(input('Latitude? '))
# longitude = float(input('Longitude? '))
# review = input('Review? ')
# locations = [
#     {
#         'name': name,
#         'latitude': latitude,
#         'longitude': longitude,
#         'review': [review],
#     },
# ]

