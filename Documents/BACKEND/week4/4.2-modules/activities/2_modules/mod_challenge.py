# REMINDER: Only do one challenge at a time! Save and test after every one.

print('Challenge 1 -------------')
# Challenge 1:
# 1. Uncomment and examine the following function code.
# 2. Add code to print the "chorus" variable from "library.py"

import library
print(library.chorus)



print('Challenge 2 -------------')
# Challenge 2:
# 1. Import the library.py file
# 2. Invoke the greeter function from library.py.
# Extra: Write an "from import" style statement to import the greeter directly.

library.greeter('errin')


print('Challenge 3 -------------')
# Challenge 3:
# Time to make your own module.
# 1. Create a new file called mymod.py
# 2. Add a print statement to it which says "mymod getting imported"
# 3. Import mymod from within this file
# 3. Create a function in the module called "myfunc"
# 4. Call the function from within this file

import mymod
mymod.myfunc()




print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the following code. Fix the typos so that it runs func1 and func2.

import anotherlib
anotherlib.func2()
anotherlib.func1()



print('Challenge 5 -------------')
# Challenge 5:
# Look around in the directories next to this file. Can you find 'file1' and
# 'file2'? Add code here to import those files

from mod import file1
from mod.deeper import file2




print('-------------')
# Bonus Challenge:
# Uncomment the following code. Can you figure out why it doesn't work?

from brokenmod import submodule
brokenmod.submodule


# Bonus Challenge:
# Take the game you made in the previous exercise. Refactor it so that
# functions are in separate files that get imported as necessary.


