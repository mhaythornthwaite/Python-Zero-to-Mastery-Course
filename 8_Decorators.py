print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------------- DECORATORS ----------------------------------
#@classmethod and @staticmethod are both decorators seen in the OOP section

# ------------------------- BACKGROUND INFORMATION ----------------------------

#functions are second class citizens they can be passed around as arguments, see below:

def say_hello():
	print('hi there, this is a useless function')
	return ''

greetings_file_location = say_hello
greetings = say_hello()

print(greetings)
print(greetings_file_location)

del say_hello

print(greetings_file_location)
# print(say_hello) this now produces an error becuase we deleted the say_hello calling card but the meat of the function still exisits is memnory because greetings is pointing to it

def f_1(func):
	print('passing through f_1 function')
	func()
	return ''

def f_2():
	print('hey Im f_2')
	return ''

#so here we're running f_1 and passing in the argument f_2 as the func parameter. This then transalates func() to f_2() which then runs the f_2() function
print(f_1(f_2))

# ------------------------- HIGHER ORDER FUNCTIONS ----------------------------
#anything that either accepts a function as a parameter or returns a function

def hof_1(func):
	func()

def hof_2():
	def internal_hof():
		print('this is a higher order function')
		return 5
	return internal_hof()

hof_2() #HOF becuase it returns a function
hof_1(hof_2) #Mega HOF becuase it's acception a function as a paremter and returns a function.


print(f'\n')
# ------------------------------- DECORATORS ----------------------------------

#decorators work a little like below:
'''
@decorator
def function():
	pass
'''
#this allows us to say, the function below this @decorator has additional abilities. Maybe it's called a decorator becuase its not actually in the function frather its above decorating it??

#defining a decorator, it has to be the following syntax

def my_first_decorator(func):
	def wrap_func():
		print('**********')
		func()
		print('**********')
	return wrap_func

@my_first_decorator
def hello():
	print('helllllooooo')

hello()

# --------- PASSING IN PARAMETERS -----------

def my_decorator(func):
	def wrap_func(*args, **kwargs):
		print('**********')
		func(*args, **kwargs)
		print('**********')
	return wrap_func

@my_decorator
def hello(name, age):
	print(f'hi there {name} you are {age}')

hello('matt', 25)

# ---------------------------- DECORATORS SYNTAX ------------------------------

def my_decorator(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

print(f'\n')
# --------------------------- PERFORMANCE EXERCISE ----------------------------

from time import time #from modules

def performance(func):
	def wrap_func(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		total_time = round(((t2 - t1) * 1000), 1)
		print(f'*******   Time elapsed {total_time}ms   *******')
		return result
	return wrap_func

@performance
def long_calc():
	for x in range(1000000):
		x * 5

long_calc()

# -------------------------- AUTHENTICATE EXERCISE ----------------------------

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
	def wrap_func(*args, **kwargs):
		if args[0]['valid']:
			fn(*args, **kwargs)
		else:
			print('you are not a valid user')
	return wrap_func


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

#I previosly ran this with user1 rather than args[0] but this will only work if the argument you pass is as the parameter user is called 'user1', else it will fail. Instead using args[0] states the first argument input is the argument we want to interogate. Therefore if we develop a new function def message_friends_2() which has multiple parameters we must state that the user dictionary needs to be the first argument.







# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')