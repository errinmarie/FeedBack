# REMINDER: Start with a print, save and test after every change.

print('Challenge 1 -------------')
# Challenge 1:
# Examine the following function code. Can you write an invocation that will
# cause it to print the phrase: "Don't Stop Believin"?

def journey(verb, action="Don't"):
    print(action, 'Stop', verb + 'in')

journey('believ')



print('Challenge 2 -------------')
# Challenge 2:
# Examine the following code.
# 1. Replace the "pass" placeholder with code that will print out each line of
# the poem.
# 2. Make the entire for-loop repeat three times, printing "Chorus 1", "Chorus
# 2", and "Chorus 3" before each time. You should do this by creating a new
# for-loop that contains the chorus for-loop. The outer for-loop should use the
# "range()" function to go through the numbers 1-3. (see hint below it)

chorus = [
    "Don't stop believin'",
    "Hold on to the feelin'",
    "Streetlight people",
]


for number in range(1, 4):
    print('Chorus', number)
    for lyric in chorus:
        print(lyric)



print('Challenge 3 -------------')
# Challenge 3:
# Write a code that asks the user to enter a rock band. Then, use the
# dictionary to display the band's most famous song. HINT: Use "input" from
# previous activities.
# Optional: Make it into a while loop that keeps on asking, and "fails
# gracefully" if there is no band with that title

bands = {
    'Journey': "Don't Stop Believin'",
    'Bon Jovi': "Livin' On a Prayer",
    'Joy Division': 'Love Will Tear Us Apart',
    'Queen': 'Bohemian Rhapsody',
    '4 Non Blondes': "What's Up?",
    'Credence Clearwater Revival': "Fortunate Son",
}







print('-------------')
# Bonus Challenge:
# The Fibonacci Sequence are the numbers where every number after the first two
# is the sum of the two preceding ones. For example:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, etc.
# 1. Write a function that will calculate the nth Fibonacci number (where n is
# a parameter), and return that value.
# 2. Come up with a "test plan" for this function.
# 3. Use "assert" to test your code. Assert is for sanity checks in code.
#
# HINT: There are several distinct approaches to this. Get one working first
# before you think of others. One might use loops, another might use
# "recursion" (calling the same function within itself), and finally there is a
# way to approximate it using a formula.
# The formula for approximation is explained here:
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section1.2


