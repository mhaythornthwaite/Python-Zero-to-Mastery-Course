print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------- FUNCTIONAL PROGRAMMING ----------------------------

#Separates out data/attributes from the processes (functions/methods) that modify them. In OOP we package both attributes and methods into a class.

#We break things down with PURE FUNCTIONS which have two rules:

#1. Given the same input it will always have the same output (remember in OOP, different class objects will give different outputs for the same methods).

#2. A function should not produce any side effects. I.e. it should only affect the input data it does not modify something else that lives somewhere else in the code, or print data to the sceen.

old_list = [1, 2, 3]

def multiply_by_2(li):
	new_li = []
	for item in li:
		new_li.append(item * 2)
	return new_li

new_list = multiply_by_2(old_list)
print(new_list)

#the above code is contained, it does not rely upon anything from the outside environment. If new_li was defined outside the function it would be changing things outside which may then have a knock on effect. 

#N.B./ A method is only a method because it lives inside a class. A function is not assigned to a class.

#below is the wizard example using functional programming, with the same result:

wizard_1 = {
	'name': 'Merlin',
	'height': 9
}

def attack_w_function(character):
	print(f'The {character["name"]} attacks at a mighty height of {character["height"]} feet.')
	return ''

attack_w_function(wizard_1)


print(f'\n')
# ------------------------ MAP, FILTER, ZIP & REDUCE --------------------------

# --------- MAP FUNCTION -----------

#used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc. using their factory functions

def map_mult_by_2(item):
	return item * 2

new_li = list(map(map_mult_by_2, [1,2,3,4]))

print(new_li)

print(f'\n')

# --------- FILTER FUNCTION -----------

#constructs an iterator from elements of an iterable for which a function returns true. In simple words, the filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

def only_odd(item):
	return item % 2 != 0

odd_list = list(filter(only_odd, [1,2,3,4,5,6]))

print(odd_list)

print(f'\n')

# --------- ZIP FUNCTION -----------

#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.

zip_li_1 = [1,2,3,4,5]
zip_li_2 = [6,7,8,9,10]
zip_li_3 = [11,12,13,14,15]

zip_tuple = tuple(zip(zip_li_1, zip_li_2, zip_li_3))
zip_list = list(zip(zip_li_1, zip_li_2, zip_li_3))

print(zip_tuple[0])
print(zip_tuple)

print(f'\n')

print(zip_list[0])
print(zip_list)

#notice how each object is a tuple but then can be strung together overall in either a list or a tuple, or a dict if 2 lists are specified to begin with.

print(f'\n')

# --------- REDUCE FUNCTION -----------

#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” module.

#reduce(function, sequence [, initial]) - > value

from functools import reduce

my_list = [1, 2, 3]

def accumulator(acc, item):
	print(acc/2, item)
	return acc/2 + item

print(reduce(accumulator, my_list, 0))

# --------- EXERCISE -----------

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def caps(item):
	return item.capitalize()

my_pets_c = list(map(caps, my_pets))

print(my_pets_c)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

zip_list = list(zip(my_strings, my_numbers))
print(zip_list)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_50(item):
	return item > 50

scores_filtered = list(filter(over_50, scores))

print(scores_filtered)


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
	return acc + item

first_pass = reduce(accumulator, my_numbers, 0)
second_pass = reduce(accumulator, scores, first_pass)

print(second_pass)


# --------------------------- LAMBDA EXPRESSIONS ------------------------------
#one time anonymous function

#typical function
def y(a, b):
	return a + b + 10
print(y(5, 2))

#lambda dunction doint the same thing
#the below is not saying that x = a number is saying x = 'a function'
x = lambda a, b: a + b + 10 
print(x(5, 2))

#above exercise without having to define unnecessary function.
print(list(filter(lambda item: item > 50, scores)))

#above exercise without having to define unnecessary function.
print(reduce(lambda acc, item: acc + item, scores, 0))

print(f'\n')
# ----------------------------- LAMBDA EXERCISE -------------------------------

my_list = [2, 5, 3, 7, 9]

print(list(map(lambda item: item * item, my_list)))

#list sorting by second value in tuple

#sorted() function has an optional parameter called 'key' which takes a function as its value. This key function transforms each element before sorting, it takes the value and returns 1 value which is then used within sort instead of the original value.

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key = lambda item: item[1]))


print(f'\n')
# ----------------------------- COMPREHENSIONS --------------------------------
#We have list, set and dictionary comprehensions. These are shorthand but they can be confusing and make the code less readable.

my_list =[]

for char in 'hello':
	my_list.append(char)

print(my_list)

# --------- LIST COMPREHENSION -----------

#now using list comprehension instead

my_list_comp = [char for char in 'hello']
print(my_list_comp)

my_list_comp_2 = [num for num in range(10)]
print(my_list_comp_2)

my_list_comp_3 = [num*2 for num in range(10)]
print(my_list_comp_3)

#so the first is an expression which is performed for 'each iterable' in 'the interable'

my_list_comp_4 = [num*2 for num in range(10) if num*2 > 8]
print(my_list_comp_4)


# --------- SET COMPREHENSION -----------

my_set_comp_4= {num*2 for num in range(10) if num*2 > 8}
print(my_set_comp_4)


# --------- DICT COMPREHENSION -----------

simple_dict = {
	'a': 2,
	's': 4
}

my_dict  = {k:v*2 for k, v in simple_dict.items()}
print(my_dict)

my_dict_2 = {k:k*2 for k in [1,2,3]}
print(my_dict_2)


# --------- COMPREHENSION EXERCISE -----------

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicates_2 = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates_2)





# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')