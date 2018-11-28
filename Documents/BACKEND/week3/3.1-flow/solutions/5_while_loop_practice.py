print('------------- Challenge 1')
# Challenge 1:

#x = 0
#while x < 10:
#    print(x)
#    x = x + 1


print('------------- Challenge 2')
# Challenge 2:


x = 11
while x < 42:
    print(x)
    x = x + 2



print('------------- Challenge 3')
# Challenge 3:
# Write the pseudocode for a while loop that calculates the "factorial" of a
# number. Examples:
# 5 factorial: 1 * 2 * 3 * 4 * 5
# 3 factorial: 1 * 2 * 3

# Initialize our variables, including one that is the factorial we want to
# calculate.
# Loop through all the integer number up until the given number
#     With each loop iteration, keep on 




print('------------- Challenge 4')
# Challenge 4:

number = 10
x = 0
factorial = 1
while x < number:
    x = x + 1
    factorial = factorial * x
print(factorial)


print('------------- Challenge 5')
# Challenge 5:
# Examine the following commented out code. See if you can answer the following
# questions about it. Then, uncomment it and see if you are right.
# 1. What will cause this loop to stop?
#    Saying something other than "no"
# 2. Why does answer start as 'no'?
#    Otherwise it will never start

answer = 'no'
while answer == 'no':
    answer = input('Done yet? ')








print('-------------')
# Bonus Challenge 1:
# Running average utility! Your task is to create a loop that keeps on asking
# the user for a number, and maintains a running average of the values the user
# entered. Stop when the user enters 'stop'.
#
# Hint: Start with pseudocode!

# "None" is a placeholder value
average = None
answer = None
while answer != 'stop':
    answer = input('Number?')
    if answer == 'stop':
        pass   # Do nothing for now...
    else:
        answer = int(answer)  # Convert to number
        if average is None:  # this is necessary to make it
            average = answer  # start with the number they enter
        else:
            average = (average + answer) / 2
    print('Running average is: ', average)






print('-------------')
# Bonus Challenge 2:
# Remember the "locations" structure? Pseudocode, then write a while loop that
# keeps on asking for new locations, and adding them to the location structure,
# until the user tells it that the user wants to quit.

locations = []
while True:    # This will loop forever!
    enter_another = input('Enter a another location? (yes or no) ')
    if enter_another == 'no':
        print('Okay, quitting')
        print(locations)
        break
    elif enter_another != 'yes':
        print('Please say "yes" or "no"')
        continue

    name = input('Location name? ')
    latitude = float(input('Latitude? '))
    longitude = float(input('Longitude? '))
    review = input('Review? ')
    new_location = {
        'name': name,
        'latitude': latitude,
        'longitude': longitude,
        'review': review,
    }
    locations.append(new_location)

