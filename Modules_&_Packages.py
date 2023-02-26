# package/__init__.py

from . import module1
from . import module2

# package/module1.py

def add(a, b):
    return a + b

 # package/module2.py

def subtract(a, b):
    return a - b

 # main.py

import package

print(package.module1.add(5, 3))
print(package.module2.subtract(5, 3))

'''output:-
8
2
'''
