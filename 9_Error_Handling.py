print(f'\n\n')
print(' ---------------- START ---------------- ')

# ----------------------------- ERROR HANDLING --------------------------------

#N.B./ ERRORS ARE CALLED EXCEPTIONS

#allows us to handle the error within the programme so if one line of code is out in the thousands we dont get an error message as the only output

#lets the python script contiue running even if there are errors

#Just a few examples of error types:
#Syntax Error
#Name Error
#Index Error
#Key Error

# ------------------------------ TRY & EXCEPT ---------------------------------

#What happens if we type a string for example, we need a 'try' handle
while True:
	try:
		#age = int(input('What is your age? '))
		age = 2
		10 / age #may produce a ValueError and ZeroDivisionError
		print(f'Your age is {age}')
	except ValueError:
		print('please enter a number')
	except ZeroDivisionError:
		print('please enter a number greater than zero')
	else:
		break
	finally:
		print('this will always run even after a break')

print(f'\n')


# ----------------------------- EXCEPT .. AS .. -------------------------------

#always best to catch errors based on specific errors so we can be more specific about what we return. We can also use the built in error message to display or be printed to the screen without cutting out the code

def mycalc(n1, n2):
	try:
		n1 / n2
	except (TypeError, ZeroDivisionError) as err: 
		print(f'youve made an error, decription: {err}')
		return ''

print(mycalc(22, 0))
print(mycalc(33, 'sdfsa'))

print('hello world')

#note that the first except that is met will always cycle back to the top, unless we have a break within that except. The only exception to this is the finally statement which is run irrespective of breaks or exceptions. 


# ---------------------------------- RAISE ------------------------------------

#what about if we want to cut it out with an error. We might just skip this whole process or do the following. So even if the code is right raise will always produce an error message:

def mycalc2(n1, n2):
	try:
		n1 / n2
		raise TypeError('Hey this is additional debugging code')
	except ZeroDivisionError:
		print('hey dude error')




# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')