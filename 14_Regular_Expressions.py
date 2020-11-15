print('\n\n')
print(' ---------------- START ---------------- ')

# --------------------------- REGULAR EXPRESSIONS -----------------------------

#useful for validation, has email been setup correctly or is the password correct. Python comes with regular expression built in module

string = 'Im searching for something, Im searching'

#returns a boolean, remember python is like english.
print('search' in string)


email = 'm.haythornthwaite@yahoo.co.uk'
print('@' in email)


print('\n')
# ----------------------------- BUILT IN MODULE -------------------------------
#Python comes with regular expression built in module

import re

#format of re.search method:  re.search(pattern, string, flags)

print(re.search('something', string))

match_object = re.search('something', string)

#match object contains all the information but the following methods access each peice of information.

print(match_object.span())
print(match_object.start())
print(match_object.end())
print(match_object.group())


print('\n')
# --------------------------------- COMPILE -----------------------------------

pattern = re.compile('Im searching')

print(pattern.search(string)) #match object (can manipulate with methods above)
print(pattern.findall(string)) #outputs each time its found
print(pattern.fullmatch(string)) #match object created if exact match
print(pattern.match(string)) #match object created if initial match


print('\n')
# -------------------------- REGULAR EXPRESSIONS 2 ----------------------------

#now comes the real power of regular expressions and it can also get quite complex. Instead of specifying an exact string we are looking for, we can search for a specified reange of charaters using regular exprssion syntax.

#use https://regex101.com/ to test regular expressions.

'''
Here is a quick summary of some useful regular expressions, there are many!!

[abc] single character of: a, b, c
[^abc] single charater except: a, b, c
[a-c] character in the range of a through to c
[a-cA-C] character in the range of a-c or A-C
. any character at all
\s white space character
\S non white space character
\. matches dot exactly
a{3,6} between 3 and 6 lots of a
[a-z]{3,6} between 3 and 6 lots of a through z
[abc]+ matches between 1 and infinite times

Combination example:
[a-z].[v] any lowercase character followed by anything followed by v

'''

password = 'fkslchellovks'

pattern = re.compile(r'[a-z].[l].[o]')
match_object2 = pattern.search(password)
print(match_object2)
print(match_object2.group())


print('\n')
# ------------------------------- VALIDATION ----------------------------------

# -------- EMAIL --------

email = 'm.haythornthwaite@yahoo.co.uk'

e_val = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
match_object3 = e_val.search(email)
print(match_object3)
print(match_object3.group())


print('\n')
# -------- PASSWROD EXERCISE --------

'''
Requirements

at least 8 characters
contains any letters, numbers or $%#@ 
has to end with a number

'''
 
password = 'fksi4857$5'

p_val = re.compile(r'^[a-zA-Z0-9$%#@]{7,}[0-9]$')
print(p_val.fullmatch(password))

match_object4 = p_val.search(password)
print(match_object4.group())





# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')