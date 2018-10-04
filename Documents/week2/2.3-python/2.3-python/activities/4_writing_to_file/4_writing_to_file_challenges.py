# Challenge 1:
# Uncomment the following code. Check that it is correctly creating a file.

# open('myfile.txt', 'w+').write('Hello file world!')



# Challenge 2:
# First, store in a variable the name of your favorite sports team (or movie).
# Then, write the code necessary to write this data to a file.




# Challenge 3:
# Using append mode ('a+'), write the names of the programming languages you
# are learning or going to learn in this course. Each language should be
# written on a separate time.




# Bonus Challenge 1:
# Write code such that every time you run this script, it will increment file
# the number found in "count.txt" by one.
# Hint: This is tricky, as you will have to read the file in first!

number = open('count.txt').read()
number = int(number)
number = number + 1
number = str(number)
open('count.txt', 'w+').write(number)

# Extra Bonus Challenge 2:
# Look up how to do "rot13" cypher. Can you write the code that reads in a
# file, applies rot13, then writes back the result to the same file?




