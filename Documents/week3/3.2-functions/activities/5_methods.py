# REMINDER: Only do one challenge at a time! Save and test after every one.


print('Challenge 1 -------------')
# Challenge 1:
# Uncomment the following code and fix the typos to practice using the list
# methods. If correct, we should see Shrek, Frozen, Titanic in that order.

my_fave_movies = []

my_fave_movies.append("Titanic")
my_fave_movies.append("Frozen")
my_fave_movies.append("Shrek")
my_fave_movies.reverse()
print(my_fave_movies)


print('Challenge 2 -------------')
# Challenge 2:
# 1. Uncomment the following code and fix the typos to practice using methods.
# 2. It should print out the dictionary keys, the phrase 'No manners!', the
# dictionary values, and then the word SHREK centered in the screen.
# Hint 1: Methods need a "." before them!
# Hint 2: Never should there be two values, functions, or variables separated
# only by space. There should always be some sort of operator, a dot, or
# something between them.

user_info = {
    'username': 'shrek',
    'location': 'swamp',
    'friend': 'donkey',
}

print(user_info.keys())
print(user_info.get('manners', 'No manners!'))
print(user_info.values())
print(user_info.get('manners', 'No manners!'))
print(user_info['username'].upper().center(80))


print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Modify it using string methods to "sanitize"
# the input. That is to say, make it so that the user can type in weird
# spellings of yes, such as "YeS", "  yes    " or "YES" to cause the program
# continue.
# Hint: Look up the documentation on string methods in Python.

answer = 'yes'
#while answer == 'yes':
#    answer = input('Stay in swamp? ')
#    answer = answer.lower()
#print('Leaving swamp...')


print('Challenge 4 -------------')
# Challenge 4:
# - Let's dip our toes further into Object Oriented Programming. We'll cover
# this in more detail in a couple lessons, but the following code ("class
# Ogre") is code that defines a new class aka data-type, with its own custom
# methods (methods being functions defined inside a class).
# - Below it, commented out, are attempts to call each of the three methods.
# Each is written incorrectly. Uncomment them, and fix each of their mistakes.
class Ogre:
    def say_name(self):
        print('My name is Shrek')

    def get_friend_name(self):
        return 'Donkey'

    def get_enemy_name(self):
        return 'Lord Farquaad'

shrek = Ogre()
shrek.say_name()
print(shrek.get_friend_name())
print(shrek.get_enemy_name())




print('Challenge 5 -------------')
# Challenge 5:
# - Time to get classy! To get more early practice with class syntax, create 3
# classes: One called LordFarquaad, one called PrincessFiona, one called
# PrinceCharming.
# - You can use the Ogre class above for reference of syntax.
# - Each should have 3 methods, each method returning different values.
#             --------------------- --------------------- ----------------------
#            |  LordFarquaad       | PrincessFiona       | PrinceCharming       |
#             --------------------- --------------------- ----------------------
# get_title  | "Lord"              | "Princess"          | "Prince"             |
# get_name   | "Lord Farquaad"     | "Princess Fiona"    | "Prince Charming"    |
# is_villain | True                | False               | True                 |

class LordFarquaad:
    def get_title(self):
        return 'Lord'

    def get_name(self):
        return 'Farquaad'

    def is_villain(self):
        return 'True'

little_dude = LordFarquaad()
print(little_dude.get_title())
print(little_dude.get_name())
print(little_dude.is_villain())


print('-------------')
# Bonus Challenge 1:
# We'll get more into the theory of OOP in a couple lessons. But until then,
# uncomment and examine the following code. See if you understand what is going
# on. See if you can refactor the 3 classes you defined in Challenge 5 to be a
# single class that takes different inputs to the `__init__` method. Once you
# have done that, see if you can create 3 instances of the class, one for each
# character that you made above.

#class Ogre:
#    def __init__(self, name, location):
#        self.name = name
#        self.location = location
#
#    def get_name(self):
#        return self.name
#
#    def get_location(self):
#        return self.location
# 
#shrek = Ogre('Shrek', 'swamp')
#print(shrek.get_name())
#print(shrek.name)
#print(shrek.get_location())
#print(shrek.location)


# Advanced Bonus Challenge:
# See if you can rewrite the bonus challenge from 2_functions.py using a class.
# Hint: Use a single class for "Location", then create many instances of that
# class for each location you can go.

