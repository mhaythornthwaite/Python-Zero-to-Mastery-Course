print(f'\n\n')
print(' ---------------- START ---------------- ')

# ----------------------------- PYTHON BASICS 2 -------------------------------

# ------------------------------ IF STATEMENTS --------------------------------

# age = int(input('How old are you? '))
age = 22

if age < 17:
  print('you are too young to drive')
elif age < 75:
  print('you are old enough to drive')
elif age > 75 and age < 90:
  print('you are possibly too old to drive')
else:
  print('you are too old to drive')

print('goodbye')

# IF STATEMENTS - logical operator
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

#truthy and falsey - all values are assumed truthy except from empty strings, tuples, 0's, none etc.
print(bool('hello')) #truthy
print(bool('')) #falsey
print(bool(0)) #falsey
print(bool(1)) #truthy

username = 'emmy123'
password = ''

if username and password:
  print('username and password is setup')
elif username:
  print('just username is setup')
elif password:
  print('just a password is setup')
else:
  print('no username or password')

print(f'thankyou\n')

#ternary operators or conditional expressions
is_friend = True
print('friends') if is_friend else print('not friends')

#short circuiting - using an or statement rather than and, it will not do the or if the condition has been satisifed with the previous

print(not(False))


# ----------------------------- GAMING EXERCISE -------------------------------

is_magician = True
is_expert = False

if is_magician and is_expert:
  print('you are a master magician')
elif is_magician and not(is_expert):
  print('at least youre getting there')
else:
  print('you need magic powers')

#is checks if the location in memory is stored in the same location


# -------------------------------- FOR LOOPS ----------------------------------

variable = [1,2,3,4,5]

for item in variable:
  item = item * 2
  print(item)

numbers = [1,2,3]
letters = ['a','b']

for x in numbers:
  for y in letters:
    print(x, y)

#for loops with dictionaries

user = {
  'name': 'matt',
  'age': 25,
  'swimmer': False
}

for x in user.items():
  print(x)

for x in user.values():
  print(x)

for x in user.keys():
  print(x)

for key, value in user.items():
  print(key, value)
 

# ---------------------------- COUNTER EXERCISE -------------------------------

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for x in my_list:
  counter = counter + x
print(counter)

# ----------------------------- RANGE FUNCTION --------------------------------
#range function with looping

y = range(0, 100, 10) #asend or decend using -1
for x in y:
  print(x)

for _ in range(0, 3):
  print('printing, note the _ is not used')

print(list(range(10)))

#almost like a nested range function
for _ in range(0, 5):
  print(list(range(0, 3)))


# --------------------------- ENUMERATE FUNCTION ------------------------------


for char in enumerate('hii'):
  print(char)

for i,char in enumerate('hii'):
  print(i,char)

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f'the index of 50 is {i}')


# ------------------------------- WHILE LOOPS ---------------------------------

i = 0
while i < 10:
  print(i)
  i = i + 1
  #break
else:
  print('finished while loop')

my_list = [1,2,3,4,5,6,7,8,9]

i = 0
while i < len(my_list):
  print(my_list[i])
  i = i + 1
  if i == 4:
    break

print(f'new code \n')

#continue jumps the lines back to start so its good for skipping code beneth it

my_list = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(my_list):
  i = i + 1
  if i > 3 and i < 7:
    continue
  print(i)


# ------------------------------ GUI EXERCISE ---------------------------------

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0,1,0,0,0,1],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# test = [0,0,0,1,0,0,0]
# for x in test:
#     if x == 0:
#       print(' ', end =''),
#     elif x == 1:
#       print('*', end =''),

#first go a bit messy but works
i = 0
for x in picture:
  for y in x:
    i = i + 1
    if i == len(x):
      if y == 0:
        print(' ')
        i = 0
      elif y == 1:
        print('*')
        i = 0
    else:
      if y == 0:
        print(' ', end ='')
      elif y == 1:
        print('*', end ='')
print(f'\n')

#solution code, much cleaner
for x in picture:
  for y in x:
    if y == 0:
      print(' ', end ='')
    else:
      print('*', end ='')
  print('')
print(f'\n')


# ------------------------- QUICK PLAY WITH ARRAYS ----------------------------

qp = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

row_number = 0
pixel_number = 0

new_list = []

for rows in qp:
  row_number = row_number + 1
  inner_list = []
  for pixels in rows:
    pixel_number = pixel_number + 1
    new_int = pixel_number + row_number
    inner_list.append(new_int)
    if pixel_number == len(rows):
      pixel_number = 0
  new_list.append(inner_list)

print(new_list)

print(f'\n')

#divide each int by 2 - here we dont actually need the list which is 'rows' but we do need the int 'pixels' because we use the values of the pixels to define the value of the new pixels which we then append to a new 'inner list'. We then append the inner list to the full 'new list' for every row we define. 

new_l = []
for rows in new_list:
  inner_l = []
  for pixels in rows:
    new_pixel = pixels / 2
    inner_l.append(new_pixel)
  new_l.append(inner_l)
print(new_l)

print(f'\n')

#here we're using y to define the numbers in the lists, we could however, define this value below the 'for y in range' and append this new value.
newlist = []
for x in range(2):
    innerlist = []
    for y in range(6):
        innerlist.append(y)
    newlist.append(innerlist)
print(newlist)
print(f'\n')


# --------------------------- DUPLICATE EXERCISE ------------------------------

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
x_count = 0
y_count = 0
cont = False

for x in some_list:
  x_count = x_count + 1
  for d in duplicate:
    if x == d:
      cont = True
      continue
    else:
      cont = False
  if cont:
    continue
  for y in some_list:
    y_count = y_count + 1
    if x_count == y_count:
      continue
    if x == y:
      duplicate.append(x)
    if y_count == len(some_list):
      y_count = 0

print(duplicate)

#solution - far more elegant
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


# ----------------------------- DEF FUNCTION() -------------------------------

#creating our own functions def - functions are useful when we want to repeat things multiple times

def say_hello():
  print('hello')

say_hello()

#aruments vs paremeters
#these are the parameters when we define the function
def hello_name(name, age, fav_pet):
  print(f'hi {name}, you are {age} and your favourite pet is a {fav_pet}')

#arguments are the actual values when we call the function
hello_name('Matt', '25', 'dog')

name_list = ['pat', 'dan', 'emma', 'alex', 'chris']
age = [23,21,33,12,14]
favpet = ['lizard', 'dog', 'cat', 'horse', 'lama']
counter = 0

for names in name_list:
  hello_name(names, age[counter], favpet[counter])
  counter = counter + 1

#previous are positional arguments
#but what about key word argument - not best practice
#say_hello(age='22', name='matt', fav_pet='dog')

#deault parameters - this is defined when we deine our function

def hi_name_v2(name='insert name'):
  print(f'hi {name}')

hi_name_v2()

#return allows us to define the variable outside of the function because the code is still returning the calculation. Otherwise it would just return none unless we define it with an expression and a variable. So npw the code below behaves as we would expect.
#n.b./ return auto exits the funtion
def sum_numbers(num1, num2):
  return num1 + num2

total = sum_numbers(10,34)
print(total)

#nested funtion, so the below funtion is completely unnecesary but it shows how it is a little complicated to do nested funtions.
#so here the last line sum_v2(num1,num2) is telling the code to run the nested funtion: sum_v2 with the inputed values num1 and num2 and return whatever this gives, this funtion then assigns n1 = num1 and n2 = num2, do the calculation n1 + n2 and return it. So makes sense when we follow through the logic but could be confusing with more complicated nested funtions

def sum_v1(num1, num2):
  def sum_v2(n1, n2):
    return n1 + n2
  return sum_v2(num1, num2)

print(sum_v1(2,3))


# ----------------------------- TESLA EXERCISE --------------------------------

def checkDriverAge(age=0):
  # age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
    # print(f'your age is {age}')
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

def_age = 94

checkDriverAge(def_age)
checkDriverAge()


# ------------------------------- DOCSTRINGS ----------------------------------

#docstrings allows us to comment inside our function that when you hover over the function it provides the description.

def explain_docstring(a='',b='',c=''):
  '''
  a = variable 1
  b = variable 2
  c = variable 3 

  This is how you describe the purpose and how to use this function.
  '''
  print(a)
  print (b)
  print(c)

help(explain_docstring)


# ---------------------------- *ARGS & **KWARGS -------------------------------

#*args and **kwargs (key word arguments) 

def super_sum(*args):
  return sum(args)

print(super_sum(1,2,3,4,5,56,6))

#**kwargs go into a dictionary and can be defined like this:

def super_sum_kwargs(*args, **kwargs):
  total = 0
  for values in kwargs.values():
    total = total + values
  return total + sum(args)

print(super_sum_kwargs(1,2,3,2,4, num1 = 3, num2 = 20))

#rule: parameters, *args, default parameters, **kwargs

li = [1,2,3,4,20,2,3,6,10,2,3,1,19]

def highest_even(input_list):
  even_list = []
  for number in input_list:
    if not number % 2:
      even_list.append(number)
  highest_even = 0
  for even_number in even_list:
    if even_number > highest_even:
      highest_even = even_number
  print(f'The highest even number in this list is {highest_even}')

highest_even(li)


# ---------------------------------- SCOPE ------------------------------------

#scope - what variables do i have access to? any variable not created inside of a function we do not have access to it outside of that function i.e. we do not have global scope

# Rules - these only appear true when we are returning a variable, if we are defining a variable which is to be used in the function we have to specifiy where it originates.
# 1. start with local - check definition of a variable in the local area.
# 2. check the parent local, do we have a parent function.
# 3. if we can not define the variable in the local area, check if it can be defined in the global area.
# 4. is it a built in python function like sum.

#this works because we are calling the variable with return
a = 10
def parent():
  #a = 100
  def child():
    #a = 1000
    return a
  return child()

print(parent())
print(a)

#This does not work because we are using the variable in calculations within the function.
# total = 0
# def counter():
#   total = total + 1
#   print(total)
# counter()

#this now works - not best practice
total = 0
def counter():
  global total
  total = total + 1
  print(total)
counter()

#pass in the parameter defined in the function
total_global = 0
def counter(total_GloLo_connector):
  total_local = total_GloLo_connector + 1
  return total_local
print(counter(counter(counter(total_global))))


# ----------------------------- NONLOCAL SCOPE --------------------------------

def outer():
  x = 'local'
  def inner():
    #nonlocal x
    x = 'nonlocal'
    print('inner:', x)
  inner()
  print('outer:', x)


outer()

print('    sdsd'.upper())




# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')