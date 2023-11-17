#importing the sys standard module, which contains functionality related 
#to the Python interpreter and its environment i.e. the system

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

