print('Challenge 1 -------------')
# Challenge #1:
# This code uses Python's built-in CSV reader to read-in a CSV file
# containing the Athletic's "40 Man Roster".
# 1. If you run it right now, it will complain about "csv" not being defined.
# Add an "import statement" to get it going by importing the "csv" module from
# the Python standard library.
# 2. CSV files store "Excel-like" data -- take a look in your editor to see
# what it looks like.
# 3. Modify the code to print the name ('Name'), uniform number ('Uniform'),
# age, weight, height, and date of birth, all on one line.

roster_file = open('athletics_40_roster.csv')
for row in csv.DictReader(roster_file):
    print(row['Name'])
    print(row['Uniform'])


print('Challenge 2 -------------')
# Challenge #2:
# 1. Use pipenv to create a new virtualenv for this activity:
#     pipenv --python 3
# 2. "Enter" the virtualenv
#     pipenv shell
# 3. Install Pint from PyPI
#     pipenv install pint
# 4. Pint is a library for converting between different unit, such as inches
#    and meters, or pounds and kilograms. Quickly read a little about Pint:
#    https://pint.readthedocs.io/en/latest/
# 5. Each of the commented lines has a mistake. Uncomment the following code
#    and fix the mistakes to get this example test usage of Pint working:

#import(pint)
#ureg = pint UnitRegistry()
#value == 3 * ureg.meter + 4 * ureg.inches
#print value




print('Challenge 3 -------------')
# Challenge #3:
# Combine Pint with the code from Activity 1 to display all the baseball
# players' weights in kilograms.
# HINT: See code below
# weight_in_pounds = float(row['Weight']) * ureg.pounds
# weight_in_kilograms = weight_in_pounds.to(ureg.kilograms)




print('Challenge 4 -------------')
# Challenge #4:
# Now, calculate the average weight of the baseball players, in kilograms.




print('-------------')
# Advanced Bonus Challenge:
# Use matplotlib to plot this data:
# https://matplotlib.org/

# Installation: Install matplotlib with pipenv as usual, although you might
# also need to install a (system-wide) dependency known as "tkinter" to get
# the graphical graph window to pop up.

# On Linux, run (anywhere):
# sudo apt-get install python3-tk

# On macOS, run (anywhere):
# brew reinstall python --with-tcl-tk

# Code: Get going by getting the following sample code running:

#import matplotlib.pyplot as plt
#x = [10, 20, 30, 40]
#y = [10**2, 20**2, 30**2, 40**2]
#plt.scatter(x, y)
#plt.show()
