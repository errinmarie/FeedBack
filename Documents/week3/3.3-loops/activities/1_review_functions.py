# REMINDER: Only do one challenge at a time! Save and test after every one.

print("test")

print('Challenge 1 -------------')
# Challenge 1:
# Write the code to "invoke" the function named lets_start
def lets_start():
    print('Time to code!')

lets_start()

print('Challenge 2 -------------')
# Challenge 2:
# 1. The goal of the following code is to "loop through" the list of Beatles
# song titles.
# 2. Uncomment the following code. It's an infinite loop! It's missing a line
# that would get it working. Add the code to get the loop to work.
# 3. Once you get it working, walk through the loop using your finger to point
# at each line. Can you "be the computer" and explain how the loop works? Don't
# shortcut this step, this is a very important skill to have when analyzing
# code!
songs = [
    'Hey Jude',
    'Come Together',
    'I Want to Hold Your Hand',
    'Yellow Submarine',
    'Yesterday',
    'A Day in the Life',
    'Here Comes the Sun',
]

i = 0
length = len(songs)
while i < length:
    song = songs[i]
    print('Beatles song is: ', song)
    i = i + 1



print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Put the following code into a function. That
# function should have a "name" as a parameter. Invoke it once using your name,
# and once using the name of a student next to you.


#name = input ("Please enter a name")

#def who_r_u(name):
#    print('Hi', name)
#who_r_u(name)



print('Challenge 4 -------------')
# Challenge 4:
# 1. Write a while loop that will count down from 100 to 48, by increments of 7.
# 2. Print each number on a separate line

i = 100

while i > 47:
    print(i)
    i = i - 7




print('Challenge 5 -------------')
# Challenge 5:
# Examine the following data. Write a while loop that will look at each item in
# the array, and output each row of data in the format of:
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





print('Challenge 6 -------------')
# Challenge 6:
# Write a while loop to do "2 steps forward, 1 step back" from 1 to 10. That
# is, it should print numbers in the following order (except on separate
# lines):
# 1 3 2 4 3 5 4 6

# HINT: It should use another variable to keep track of alternation between
# "two steps forward" and "one step back". Within the while loop it should have
# an if-statement. Consider using Boolean values True and False.



print('Challenge 7 -------------')
# Challenge 7:
# Uncomment the following code. Examine how it works.
#
# Then, modify it in the following way:
# 1. Put it into a function
# 2. Give that function an argument that consists of the valid choices
# (presently, only 'quit'). Have it keep on asking until it gets a valid
# choice.
# 3. Return the option the user selected.
# 4. Add print code to remind the user of the valid choices.

#answer = 'quit'
#while answer != 'quit':
#    answer = input('Choice? ')


print('-------------')
# Bonus Challenge:
# Using the skills you have learned so far, write a "hang-man" word guessing
# game! We've written some code to get you started. If you are unfamiliar with
# the game "Hangman", look it up, or read the summary below:
# Each turn, the user must choose a letter to guess. Whenever a letter is
# guessed, that letter should be filled in. The player wins when they have
# guessed all the letters. The player loses if they run out of wrong-guesses.

word_to_guess = 'juxtaposition'
guessed_letters = []

def print_word():
    # We'll be learning about for-loops next!
    censored_word = ''
    for letter in word_to_guess:
        if letter not in guessed_letters:
            letter = '_'
        censored_word = censored_word + letter + ' '
    print(censored_word)


