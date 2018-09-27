# Loop through elements in an array
menu = ['spam', 'spam', 'eggs', 'spam']
for item in menu:
    print('Menu item:', item)

# Loop through numbers 0-9
for i in range(10):
    print(i)

# Loop through keys in a dictionary
translations = {
    'dog': 'cachorro',
    'cat': 'gato',
    'bread': 'pão',
    'lettuce': 'alface',
    'tomato': 'tomate',
    'tofu': 'tofu',
}

for english_word in translations:
    portuguese_word = translations[english_word]
    print(english_word, 'is', portuguese_word, 'in Portuguese')

# Alternate, cleaner method to loop through dictionary, using "items()" method
# in dictionary
for english_word, portuguese_word in translations.items():
    print(english_word, 'is', portuguese_word, 'in Portuguese')

