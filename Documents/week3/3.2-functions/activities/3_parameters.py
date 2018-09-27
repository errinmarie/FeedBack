# REMINDER: Only do one challenge at a time! Save and test after every one.

print('test')

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named challenge_1, providing your
# name, such that when you run this file it greets you.

def challenge_1(name='Errin'):
    print('Hello', name, '!')

challenge_1()

print('Challenge 2 -------------')
# Challenge 2:
# 1. Uncomment the following code.
# 2. Many of these functions and invocation have typos or mistakes. Fix all the
# mistakes and typos to get the code running.
# (When running correctly, it should print dialog from a popular movie.)

def func_1(name=None):
    print(name, ':', "I can't feel my body")

def func_2(name=None, other_name=None):
    print(name, ':', other_name, ',', 'listen to me!')

def func_3(quality='best', item='burrito'):
    print('Winning that', item, 'was the', quality, 'thing.')

def func_4(name=None, phrase=None):
    print(name, ":", "I promise.", phrase, "," "Jack.", phrase)


func_1(name='Rose')
func_2(name='Jack', other_name='Rose')
func_3(item='ticket')
func_4(name="Rose", phrase="I'll never let go")


print('Challenge 3 -------------')
# Challenge 3:
# 1. Examine the function written that performs addition. Uncomment the code to
# invoke it.
# 2. Write another invocation to test it out with different values.
# 3. Use a similar pattern to write functions that do 5 other operations, and
# invocations for each one: subtraction, multiplication, division,
# exponentiation, and modulus

def addition(a=0, b=0):
    print(a + b)

addition(a=10, b=15)
addition(a=20, b=25)

def subtraction(a=0, b=0):
    print(a - b)
subtraction(a=20, b=25)

def multiplication(a=0, b=0):
    print(a * b)
multiplication(a=20, b=25)

def division(a=0, b=0):
    print(a / b)
division(a=20, b=25)

def remainder(a=0, b=0):
    print(a % b)
remainder(a=20, b=2)



print('Challenge 4 -------------')
# Challenge 4:
# 1. Write a function called "asker" that has a parameter called
# "acceptable_options".
# 2. At first, it should simply print the parameter.
# 3. Then, write an invocation of the function, such that this parameter is
# assigned to a list.
# 4. Finally, add a while loop to the function such that it keeps on asking for
# user input UNTIL that input is something contained within that list.
# HINT: You'll use "while", "input", and the "in" operator or the "not in"
# operator (for checking inclusion within the list)


#def challenge_1(name='Errin'):
#    print('Hello', name, '!')
#challenge_1()

#func_2(name='Jack', other_name='Rose')

def asker(acceptable_options="name"):
    print(acceptable_options)
    name = input("What is your name?")

asker(acceptable_options=["Errin", "Matt", "Mary"])

input







print('-------------')
# Bonus Challenge:
# Write a function that has a dict parameter that is a "menu" of options. This
# dict should have keys that consist of the text that can be entered, and
# values that consist of functions.
# - When the user selects an item from the menu, it should invoke that
# function.
# - If the user enters an invalid choice, it should ask again.

