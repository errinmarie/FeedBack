print('Challenge 1 -------------')
# Challenge 1:
# Uncomment the following code. Fix the mistakes to get it to say.
# It's as easy as 0
# It's as easy as 1
# It's as easy as 2

for x in range(3):
    print("It's as easy as", x)




print('Challenge 2 -------------')
# Challenge 2:
# Using the range function, write a for loop that prints out the following
# numbers (each on separate lines):
# a. 0 1 2 3 4
# b. 3 4 5 6 7
# c. 9 11 13 15
# d. 15 14 13 12 11

#for n in range(5):
#    print(n)

#for n in range(3, 8):
#    print(n)

#for n in range(9, 16, 2):
#    print(n)

#for n in range(15, 10, -1):
#    print(n)



print('Challenge 3 -------------')
# Challenge 3:
# Loop through the following dictionary displaying the word in English and the
# word in Portuguese. The first item should be displayed like:
# dog : cachorro
# Hint: Use translations.items() to loop
translations = {
    'dog': 'cachorro',
    'cat': 'gato',
    'bread': 'pão',
    'lettuce': 'alface',
    'tomato': 'tomate',
    'tofu': 'tofu',
}

for key, value in translations.items():
    print(key, ': ', value)


print('Challenge 4 -------------')
# Challenge 4:
# 1. Use a for in loop and range to loop through the following foods, printing
# out each number so you get the result:
#     1 banana
#     2 apple
#     3 pear

foods = ['banana' 'apple' 'pear']

for n, food in foods:
    print(n(1, 4))
    print(food)
    





# 2. Refactor your loop to use "enumerate" (Google Python enumerate)
fave_foods = [
    'banana',
    'apple',
    'pear',
]






print('Challenge 5 -------------')
# Challenge 5:
# Time to practice the "in" operator. This is NOT RELATED to for loops, but
# good to know, and easily confused with for-loops.

# 1. Uncomment and try the following code as an example:
#if 'banana' in fave_foods:
#    print('Banana is a favorite food')
#else:
#    print('Banana is not a favorite food')

# 2. Write an if statement to check if bread is a favorite food
# 3. Write an if statement to check if bread is in the English Portuguese
# dictionary
# 4. Write an if statement using "in" and "range" to check if 55 is an odd
# number between 51 and 100 (Hint: use range)




print('-------------')
# Bonus challenge:
# The following superheroes are in a list. Write for-loops that prints all "vs"
# match-ups between the super heroes. For example, "Magneto vs. Wonder Woman". 
# 1. It should print all possible match-ups.
# 2. It should not print vs themselves, e.g. "Spiderman vs Spiderman"
superheroes = [
    'Wonder Woman',
    'Spiderman',
    'Magneto',
    'Catwoman',
]

