print(f'\n\n')
print(' ---------------- START ---------------- ')

# -------------------------------- FILE I/O -----------------------------------

#file I/O stands for 'file Input/Output' so reading and writing files

#so its inputing something from the outside world and then outputing somethign to the outside world (such as a website)


# -------- READ --------

my_file = open('test.txt') #note this is a function not a statement

print(my_file) #prints object location

print(my_file.read()) #prints the document itself

#python uses this idea of a cursor (called stream) to read a file, once the cursor has reached the end with the read method it remains there, seek moves this cursor


my_file.seek(0)
print(my_file.read())

#so seek effecrively works like an index on the characters

my_file.seek(6)
print(my_file.read())

my_file.close()


# -------- READLINE & READLINES --------

my_file2 = open('test_files_module13/test2.txt')
print(my_file2.readline())
print(my_file2.readline())

print('\n')

my_file2.seek(0)
print(my_file2.readlines())


my_file2.close()

#n.b./ .close() is good practice to prevent more editing occuring 


# ----------------------------- WITH STATEMENT --------------------------------

#this is the more correct syntax to read/write files. We no longer need to close the file after opening and we can specify the mode:

'''
 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.
         .

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.
         .

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.
         .

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
'''

#read never truncates, will overwrite, stream always at begining
#write always truncates, will overwrite, stream always at begining
#append never truncates, will not overwrite, stream always at end


# -------- READ 'r' --------

with open('test.txt', mode='r') as my_file:
	print(my_file.readline())


# -------- READ+ 'r+' --------

with open('test_files_module13/test4.txt', mode='r+') as my_file:
	my_file.write(':)')


# -------- WRITE 'w' --------


with open('test_files_module13/test3.txt', mode='w') as my_file:
	text = my_file.write('hi this file was generated in the write mode')
	print(text)


# -------- APPEND 'a' --------

with open('test_files_module13/test5.txt', mode='a') as my_file:
	my_file.write('\nhi this is an added line with the append method')


# -------- APPEND AND READ 'a+' --------

with open('test_files_module13/test6.txt', mode='a+') as my_file:
	my_file.write('\nhi this is an added line with the append+ method')
	my_file.seek(0)
	print(my_file.readline())


# -------- TESTER FILE --------

with open('test_files_module13/test7.txt', mode='r+') as my_file:
	my_file.write(':)')


# ------------------------------- FILE PATHS ----------------------------------

#n.b./ can go back a directory by '$cd ..' 


# -------- RELATIVE FILE PATH --------

#these are all seen above which point to the directory and file of interest given the current .py file path


# -------- RELATIVE FILE PATH BACK ONE --------

#n.b./ can go back a directory by '$cd ..' 
#the same can be done with a relative path ../ before the file takes you back one ditectory. This ccan be done at any time as many times as you want to find your target directory.

with open('../Module_13_test_area/test9.txt', mode='r') as my_file:
	print(my_file.readline())


# -------- ABSOLUTE FILE PATH --------

#the file below is being opened with the absolute path. Long code but if the file you're after exists in a completely different area it will be required.

with open('C:/Users/mhayt/Documents/Software Developer - Python/Python Basics/test_files_module13/test8.txt', mode='r') as my_file:
	print(my_file.readline())


# ------------------------------ TRY STATEMENT --------------------------------

#common practice to put a file IO statement in a try statement

try:
	with open('test00.txt', mode='r') as my_file:
		print(my_file.readline())
except FileNotFoundError as err: 
	print(f'youve made an error, decription: {err}')
except IOError as err: 
	print(f'youve made an error, decription: {err}')

print('\n')
# --------------------------- TRANSLATOR EXERCISE -----------------------------

from translate import Translator


# -------- QUICK TEST --------

english_text = 'Hi I am learning to code, how are you? Sneaky, I am 25 years old.'

french = Translator(to_lang="fr")
translation = french.translate(english_text)
print(translation)


# -------- EXERCISE --------

#solution provided

with open('translation_files_m13/english_file2.txt', mode='r+') as e_file:
	x = e_file.read()
	french = Translator(to_lang="fr")
	translation = french.translate(x)
	with open('translation_files_m13/french_file2.txt', mode='w+') as f_file:
		f_file.write(translation)


#this method is actually a bit more elegant and handles each line better than the solution

with open('translation_files_m13/english_file.txt', mode='r+') as e_file:
	with open('translation_files_m13/french_file.txt', mode='w+') as f_file:
		for line in e_file:
			french = Translator(to_lang="fr")
			translation = french.translate(line)
			f_file.write(f'{translation}\n')





# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')