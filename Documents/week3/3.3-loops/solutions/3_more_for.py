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
# a. 0 1 2 3 4
for i in range(5):
    print(i)

# b. 3 4 5 6 7
for i in range(3, 8):
    print(i)

# c. 9 11 13 15
for i in range(9, 16, 2):
    print(i)

# d. 15 14 13 12 11
for i in range(15, 10, -1):
    print(i)


print('Challenge 3 -------------')
# Challenge 3:
translations = {
    'dog': 'cachorro',
    'cat': 'gato',
    'bread': 'pão',
    'lettuce': 'alface',
    'tomato': 'tomate',
    'tofu': 'tofu',
}
for en, pt in translations.items():
    print(en, ':', pt)


print('Challenge 4 -------------')
# Challenge 4:
fave_foods = [
    'banana',
    'apple',
    'pear',
]
for i in range(len(fave_foods)):
    food = fave_foods[i]
    print(i + 1, food)

for i, food in enumerate(fave_foods):
    print(i + 1, food)

print('Challenge 5 -------------')
# Challenge 5:

if 'banana' in fave_foods:
    print('Banana is a favorite food')
else:
    print('Banana is not a favorite food')

# 2. Write an if statement to check if bread is a favorite food
if 'bread' in fave_foods:
    print('Bread is a favorite food')
else:
    print('Bread is not a favorite food')

# 3. Write an if statement to check if bread is in the dictionary
if 'bread' in translations:
    print('Bread is in the dictionary')
else:
    print('Bread is not in the dictionary')

# 4. Write an if statement to check if 55 is an odd number between 51 and 100
if 55 in range(51, 100, 2):
    print('55 is an odd number between 51')
else:
    print('55 is not an odd number between 51')





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

for hero1 in superheroes:
    for hero2 in superheroes:
        if hero1 != hero2:
            print(hero1, 'vs', hero2)

