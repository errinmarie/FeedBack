# REMINDER: Only do one challenge at a time! Save and test after every one.


print('Challenge 1 -------------')
data = [
    {
        'name': 'Girls just wanna have fun.',
        'artist': 'Cindy Lauper',
    },
    {
        'name': 'Giving it up for your love',
        'artist': 'Delbert McClinton',
    },
]

import pprint
pprint.pprint('Hello world')
pprint.pprint(data, indent=2, width=30)





print('Challenge 2 -------------')
# Challenge 2:
import time
import subprocess
import datetime
import random
print(random.randint(5, 10))
data = ['a', 'b', 'c']
random.shuffle(data)
print(data)



print('Challenge 3 -------------')
import json
example_json = open('example_json.json').read()
d = json.loads(example_json)
print(d['a'])


print('Challenge 4 -------------')
# Challenge 4:
import sys
# just interesting stuff
cli_args = sys.argv[1:]
print(cli_args)



print('Challenge 5 -------------')
subprocess.run('ls')
output = subprocess.check_output('ls')
print('this is output', output)


print('Challenge 6 -------------')
filenames = output.split()
for filename in filenames:
    # The "decode" removes the 'b' - changing from the "bytes" datatype
    # to an actual string of text
    print(filename.decode())



