print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------------- DEBUGGING -----------------------------------
'''

Linting: this is in IDE's which underline these errors 

IDE's: Have formatting built in

Learn to read errors: What do the error types mean such as TypeError or SyntaxError

pdb: python debugger (built in module)
	a: gives you arguments
	w: context of the current line it is operating
	next: moves you on to the next line
	continue: run until you hit an error or end

This is all very useful because you can also interactively change attributes to test whether it then runs for example with a defferent lass type

'''


import pdb

def add(n1, n4):
	pdb.set_trace()
	return n1 + n2

add(1, 'dsads')



# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')