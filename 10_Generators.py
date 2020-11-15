print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------------ GENERATORS -----------------------------------
#generate a sequence of values over time, we've seen this before in range()

#has the ability to pause and resume function

def make_list(n):
	result = []
	for i in range(n):
		result.append(i)
	return result

#take note this works because we have a return and then the result. So if we didnt have return the list we just made that list will be stuck in the local function.

my_list = make_list(10)

#when the function has run we save the list in memory. But the important thing is the range(n) is producing each number and then once its done with that number its thrown away, it's not saved to memory

print(my_list)

#so when we have massive lists its more efficient to go one by one with a generator rather than create or load the entire list.


# ---------------------------------- YIELD ------------------------------------

#yield pauses the function and comes back to it when we call it

def generator_function(n):
	for i in range(n):
		yield i

for item in generator_function(4):
	print(item)

#so above we looped through the list above (it could have been massive) but instead of creating the list and saving to memory all in one go, we performed our task which is print, one by one.

print(f'\n')
# ---------------------------------- NEXT -------------------------------------

def generator_function(n):
	for i in range(n):
		yield i**2

g = generator_function(10)

print(g) #returns the generator object location

print(next(g))
print(next(g))
print(next(g))
print(next(g))

#next is simply saying I want the first, second, third, forth (etc. in this case) value in the generator_function(n) iterable.


# --------------------------- PERFORMANCE EXAMPLE -----------------------------

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
def long_time(n):
	print('generator')
	for i in range(n):
		i * 5

@performance
def long_time_2(n):
	print('generator and list in memory')
	for i in list(range(n)):
		i * 5

#so the main difference in the second on is it has to first make the list(range(n)) and then iterate over it. Whereas the first one goes through range(n) a generator, therefore going through each one and throwning away the old values.

t = 1000000

long_time(t)
long_time_2(t)


# ----------------------------- EXAMPLE SYNTAX --------------------------------

def gen_fun(n):
	for i in range(n):
		yield i

for item in gen_fun(100):
	pass


# ------------------------------- MY OWN TEST ---------------------------------

#all im doing here is instead of using range im using the template for a generator function which is simply replicating range() (using range). Therefore it is slower than the two previous examples but the list version is still slower than the simple generator fucntion

@performance
def long_time_3(n):
	print('generator of range()')
	for i in gen_fun(n):
		i * 5

@performance
def long_time_4(n):
	print('list from generator of range()')
	for i in list(gen_fun(n)):
		i * 5


t = 1000000

long_time_3(t)
long_time_4(t)

print(f'\n')
# ---------------------- UNDER THE HOOD OF GENERATORS -------------------------

#iter() function creates an bject which can be iterated one object at a time (requires the getitem or next function otherwise an error is returned)
#so while True simply sets up the loop which will loop forever until break is implimented. Try handle is part of the while loop. And then StopIteration is the error message received when there is no next(iterator) so we then break.

#this is how regular for loops work under the hood

def special_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			print(iterator)
			next(iterator)
		except StopIteration:
			break

special_for([1,2,3])

# ------------ QUICK TEST ------------ 

test = iter([1,2])
print(next(test))
print(next(test))
# print(next(test)) this produces a StopIteration error message


# -------------------- CREATING OWN RANGE CLASS EXERCISE ----------------------

class MyGen():
	def __init__(self, last):
		self.last = last

	current = 0

	def __iter__(self):
		return self

	def __next__(self):
		if MyGen.current < self.last:
			num = MyGen.current
			MyGen.current += 1
			return num
		raise StopIteration

gen = MyGen(4)
for i in gen:
	print(i)


# ----------------------- FIBONACCI NUMBERS EXERCISE --------------------------

print(f'\n')

# ----- USING LISTS -----

def fib(n):
	fib_seq = [0,1]
	new_fib = 0
	for i in range(n-2):
		new_fib = fib_seq[i] + fib_seq[i+1]
		fib_seq.append(new_fib)
	return fib_seq

exercise = fib(8)
print(exercise)		

# ----- USING GENERATORS -----

def fib_gen(n):
	print(0)
	print(1)
	fib_i0 = 0
	fib_i1 = 1
	new_fib = 0
	for i in range(n-2):
		new_fib = fib_i0 + fib_i1
		fib_i0 = fib_i1
		fib_i1 = new_fib
		print(new_fib)

fib_gen(8)
print(f'\n')

# ----- SOLUTION USING GENERATORS -----

def fib_gen_sol(n):
	a = 0 
	b = 1
	for i in range(n):
		print(a)
		temp = a
		a = b
		b = b + temp

fib_gen_sol(12)


# ----- SOLUTION USING LISTS -----

def fib_list_sol(n):
	fib = [] 
	a = 0
	b = 1
	for i in range(n):
		fib.append(a)
		temp = a
		a = b
		b = b + temp
	return fib

fib_list = fib_list_sol(12)
print(fib_list)



# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')