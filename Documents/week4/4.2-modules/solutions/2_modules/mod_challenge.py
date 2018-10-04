# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# Uncomment and examine the following function code. Add code to print the
# "chorus" variable from "library.py"
import library
print(library.chorus)


print('Challenge 2 -------------')
# Challenge 2:
# Invoke the greeter function from library.py. Also, write an "from import"
# style statement to import the greeter directly.
library.greeter('alice')
from library import greeter
greeter('bob')



print('Challenge 3 -------------')
# Challenge 3:
# Uncomment the following code. Fix the typos so that it runs func1 and func2.

import anotherlib
from anotherlib import func2
anotherlib.func1()
func2()



print('Challenge 4 -------------')
# Challenge 4:
# Look around in the directories next to this file. Can you find 'file1' and
# 'file2'? Add code here to import those files
from mod import file1
from mod.deeper import file2




print('Challenge 5 -------------')
# Challenge 5:
# Uncomment the following code. Can you figure out why it doesn't work?
# ANSWER: Need an __init__.py in brokenmod that imports submodule
import brokenmod
brokenmod.submodule

print('-------------')
# Bonus Challenge:
# Take the game you made in the previous exercise. Refactor it so that
# functions are in separate files that get imported as necessary.


