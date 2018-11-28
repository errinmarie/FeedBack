# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Can you write the code to do a for-loop across "fave_things" printing out
# each item?
fave_things = [
    'cats',
    'doggos',
    'books',
]

for item in fave_things:
    print(item)


print('Challenge 2 -------------')
# Challenge 2:
# Uncomment the following code. Fix the typos!

for item in fave_things:
    print('i like', item)

for item in fave_things:
    print('i like', item)

for item in fave_things:
    print('i like', item)



print('Challenge 3 -------------')
# Challenge 3:
# 1. Let's repeat Challenge 5 from the previous activity, only using the
# superior for loops. (It's okay if you didn't get to it)
# 2. Examine the following data. Write a for loop that will look at each item
# in the array, and output each row of data in the format of:
# Top hit from the 60s: I'm a believer ...  Artist: The Monkees.
data = [
    ["I'm a Believer", 'The Monkees'],
    ['Respect', 'Aretha Franklin'],
    ["(I Can't No) Satisfaction", 'The Rolling Stones'],
    ['Good Vibrations', 'The Beach Boys'],
    ['My Girl', 'The Temptations'],
    ["I Can't Stop Loving You", 'Ray Charles'],
    ["Blowin' in the Wind", 'Bob Dylan'],
]

for row in data:
    song = row[0]
    artist = row[1]
    print('Top hit from the 60s:', song, 'Artist:', artist)

for song, artist in data:
    print('Top hit from the 60s:', song, 'Artist:', artist)


# Hint: Once you get it working, see if you can refactor it using the following
# Python trick:
# for song, artist in data:



print('Challenge 4 -------------')
# Challenge 4:
# Time to handle more complicated (and realistic) data structures.
# 1. Examine the following data. What data types are we dealing with?
# 2. Write a for loop that goes through them, printing out information about
# each made-up product. The format should match the example below:
#
# --- Product ---
# Name: Nodular Coagulator
# Supplied by: Wisozk Inc
# Available: 261 (at $10.47 a piece)
# ---------------
data = [
    {
        'product_name': 'Nodular Coagulator',
        'supplier': 'Wisozk Inc',
        'quantity': 261,
        'unit_cost': '$10.47',
    },
    {
        'product_name': 'Juniperus Testator',
        'supplier': 'Keebler-Hilpert',
        'quantity': 292,
        'unit_cost': '$8.74',
    },
    {
        'product_name': 'Dextro Consolidator',
        'supplier': 'Schmitt-Weissnat',
        'quantity': 211,
        'unit_cost': '$20.53',
    },
]

for dict in data:
    print('---Product---')
    print('Name: ', dict['product_name'])
    print('Supplied by: ', dict['supplier'])
    print('Available: ', dict['quantity'], '(at ', dict['unit_cost'], 'a piece)') 
        





print('-------------')
# Bonus Challenges:
# Refactor the previous challenge to use Python "f-strings".
# For example, using a multi-line string:
# results = f"""
#    Some text: {variable_name}
#    Other text: {dict_name['key']}
# """
# An article describing: https://www.blog.pythonlibrary.org/2018/03/13/python-3-an-intro-to-f-strings/
# A much more thorough article: https://realpython.com/python-f-strings/

for dict in data:
    print(f'''---Product---'
Name: {dict['product_name']}
Supplied by: {dict['supplier']}
Available: {dict['quantity']} (at {dict['unit_cost']} a piece)
-------------------------------''')

print('-------------')
# Advanced Bonus Challenges:
# The "mode" of a data set is the item in the data that appears the most often.
# Challenge 1. Can you write a for loop that processes the mode of a list of numbers?

# Challenge 2. Python challenge: Look up the built-in "max" function. Can you,
# in one short line, use the "max" function to print the mode?

numbers = [
    1, 547, 100, 3123, 42, 12814, 42, 364, 317, 42, 38747, 213, 1, 42, 134,
    547, 213, 132.3, 904, 348, 12, 94, 238, 448,
]
