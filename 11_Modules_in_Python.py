print(f'\n\n')
print(' ---------------- START ---------------- ')

# -------------------------------- MODULES ------------------------------------

#each .py file is effectively a module, but the main thing that specifies a mpdule is a module has a series of functions, i.e. it is not running anything directly. N.B./ a package is a folder containing modules

# ---------------------- IMPORTING MODULES & FUNCTIONS ------------------------

# module import
import Modules.utilities
print(Modules.utilities.multiply(1,2))

#module import but cleaner 
from Modules import utilities
print(utilities.multiply(1,2))

#function import (note these override existing functions)
from Modules.utilities import multiply
print(multiply(1,2))


# -------- ONLY RUNNING __main__ FILE --------

print(__name__) #__main__ is given to the file which is being directly run

if __name__ == '__main__':
	print('use me to only run the main python file')


# ------------------------------- CLASS TYPES ---------------------------------
#testing what class types are returned for classes built in the main project and imported modules.

test = utilities.Util('Im a utility')
print(type(test))

class MainClass:
	pass

test2 = MainClass()
print(type(test2))

print(f'\n')
# ---------------------------- BUILT IN MODULES -------------------------------

# -------- IMPORTING RANDOM --------

import random

print(random)

#help(random) #provides information on the module
print(dir(random)) #prints all the functions in module

print(random.random())
print(random.randint(1,4))
print(random.choice([1,5,6,7,8,9]))
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)
print(random.uniform(1,4))

print(f'\n')

# -------- IMPORTING FUNCTIONS FROM RANDOM --------

#notice how we now dont need to specify that the functions live with the random module, they exist directly and we can call them what we like with the as statement

from random import randint
from random import uniform as randflt

print(randint(1,10))
print(randflt(1,10))


# -------- IMPORTING SYS --------

import sys

first_param = sys.argv[1]
second_param = sys.argv[2]

print(f'hi my name is {first_param}, and I am {second_param} years old')


# --------------------------- INSTALLING PACKAGES -----------------------------

#installing using pip is used in the command prompt. These can be found in pypi (Python Package Index) and countains thousands of packages which can be installed in the command line and then used by importing them. This is the power of python. 

#N.B./ If we get an error message we can install using the following command:
#$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>


# -------- PIPENV --------

#this allows the user to install packages bases on specific projects. Often in folder called venv

print(f'\n')
# ----------------------------- USEFUL MODULES --------------------------------

#not exhaustive list of some frequently used, useful modules.


# ------------------------- SPECIALISED DATA TYPES ----------------------------

# -------- COLLECTION MODULE --------

from collections import Counter, defaultdict, OrderedDict


# -------- COUNTER CLASS --------

li = [1,2,7,4,5,6,7,7]

#notice Counter is a class so its turning this list into a Counter class
li_c = Counter(li)
print(li_c) 

print(li_c[7]) #how many 7's do I have?

print(Counter('how many letters')) #can be do for strings as well


# -------- DEFAULTDICT FUNC --------

dictionary = {'a': 1, 'b': 2}
print(dictionary['a'])

#if you are accessing a ket that doesnt exist, applying defaultdict will prevent error messages
dictionary = defaultdict(lambda:5, {'a': 1, 'b': 2})
print(dictionary['c'])


# -------- ORDEREDDICT --------

od = OrderedDict()
od['a'] = 1
od['b'] = 2

od2 = OrderedDict()
od2['b'] = 2
od2['a'] = 1

print(od == od2) #order matters to OrderedDict class type so False


d = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

print(d == d2) #order doesnt matter to dict class so True


# -------- DATETIME --------

import datetime as dt

print(dt.time(20,7,0))
print(dt.date.today())


# -------- ARRAY --------

#more performant than a list

from array import array

ar = array('i', [1,2,3])

print(ar)
print(ar[0])




# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')