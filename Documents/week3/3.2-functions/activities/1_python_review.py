# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Create 3 variables. Store in them your name, your favorite color, and how
# many hours of sleep you got last night. Print out all 3 values using "print".

name = 'Errin'
favorite_color = 'yellow'
hours_sleep = '6'
print(name + favorite_color + hours_sleep)




print('Challenge 2 -------------')
# Challenge 2:
# - Create a list of your favorite book authors
# - Put it into a variable called "authors_list"

authors_list = ['Marian Keyes', 'Sophie Kinsella', 'Alex Haley']
print(authors_list)





print('Challenge 3 -------------')
# Challenge 3:
# Write an "if-statement" to check if the top author on that list is equal to
# "Douglas Adams". If it is, print "Don't panic!". Otherwise, print "Panic!"
# Hint: The very first author is accessible with authors_list[0]

if authors_list[0] == "Douglas Adams":
    print("Don't panic!")
else:
    print("Panic!")




print('Challenge 4 -------------')
# Challenge 4:
# 1. Uncomment the provided code. What does it do?
# 2. Using a while loop, use this as a clue to write code to "loop through"
# your favorite authors list, printing each one on a separate line, along with
# its index.



authors_list = ['Marian Keyes', 'Sophie Kinsella', 'Alex Haley']

for author in authors_list:
    print(author)

i = 0
length = len(authors_list)
while i < length:
    print(i, authors_list[i])
    i = i + 1


print('Challenge 5 -------------')
# Challenge 5:
# 1. Uncomment the provided code. What does it do?
# 2. Using this a start, create a while loop that keeps on looping until the
# user says "Stop". Have it print back whatever they say each time it loops.

#user_input = input('Stop? ')







print('-------------')
# Bonus Challenge:
# Create a chat bot!
# - Using a dictionary and a while / input loop, every time a user enters text
# check in the dictionary for a pre-set set of replies (e.g. "hi" responds with
# "hello").
# - It should exit if the person says "bye" or something similar.
# - How can you make it more robust and respond to more spelling or grammar
# differences?


