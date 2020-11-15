print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------------ GUESSING GAME --------------------------------

#importing required functions
from sys import argv
from random import randint

#defining the guessing bounds
lower = int(argv[1])
upper = int(argv[2])

answer = randint(lower, upper)

#generating a guessing fuction that will only accept int between given bounds.
def guess_num():
	while True:
		try:
			print(f'please guess a number between {lower} and {upper}: ', end ='')
			guess = int(input())
		except ValueError:
			print('Thats not a number, ', end ='')
			continue
		if guess < lower or guess > upper:
			print(f'That number is outside the range ', end ='')
		else:
			return guess
			break

#initial guess
guess = guess_num()

#are you right?
count = 0 
while True:
	if guess != answer:
		print('unlucky thats not the right answer, try again:')
		print(f'\n')
		count = count + 1
		guess = guess_num()
		if count == 4: #providing a clue by narrowing the range
			r = answer - int((upper - lower)/2)
			new_lower =  randint(r, answer)
			new_upper = new_lower + int((upper - lower)/2)
			print(f'heres a clue, the answer is between {new_lower} and {new_upper}')
			#continue
	else:
		print('WELL DONE YOU GOT IT RIGHT!!!')
		break


# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')