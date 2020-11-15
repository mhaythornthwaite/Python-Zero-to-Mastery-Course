print(f'\n\n')
print(' ---------------- START ---------------- ')

# ------------------------------ PYTHON BASICS --------------------------------

# x = input('Hi there, what is your name? ')
# y = input('Hello ' + x + ' how old are you? ')
# print('Nice to meet you ' + x +', a ' + y + ' year old.') 
# Formatted string version with f to begin with
# print(f'Nice to meet you {x}, a {y} year old')

xx = 2.5 + 4.5 
print(xx)
print(type(xx))
print(type(2.5 + 4.5))
print(3 ** 20) 
print(5 % 3)

print(round(3.5545))
print(abs(-32.2))

iq = 100
user_age = iq / 5
print(user_age)

# augmented assingment operator
xy = 5
xy += 2
print(xy)


# --------------------------------- STRINGS -----------------------------------

user = 'thwaitey'
password = 'flvmbeu2'
long_string = ''' 
hello
there
'''
print(long_string)

# String Concatenation - basically means adding strings together
print(user + ' ' + password)

# Type Conversion
print(type(str(int(100))))
print('\n')

# Escape Sequence - using '/" in a string
weather = '\"It\'s sunny\" said Matt'
print(weather)
comment = '\t adds a tab \n adds a new line'
print(comment)

# String Indexes [start:stop:stepover]
bookshelf = 'all about books'
print('\n')
print(bookshelf[::-1])

#Strings are immutable meaning we cannot change parts of them we can only reassign the entire string, or create a new string, see the error below
# number = '5603'
# number[2] = 9
# print(number)

print(bookshelf[0:len(bookshelf)])

quote = 'to be or not to be'
print(quote.find('be'))
new_quote = quote.replace('be', 'me')
print(new_quote)


# -------------------------------- BOOLEANS -----------------------------------

#booleans can either be true or False
male = True
female = False 
print(bool(male))

#quick exercise
# birth_year = input('what year were you born? ')
# birth_year_int = int(birth_year)
# age = 2019 - birth_year_int
# print(f'your age is {age}')

#password checker exercise
# username = input('Select a username ')
# password = input('Select a password ')
# password_length = len(password)
# hidden_password = '*' * password_length
# print(f'Hi {username}, your password: {hidden_password}, is {password_length} characters long')


# ---------------------------------- LISTS ------------------------------------

#Lists - a form of array
li = [1,2,3,'apple',5,6]
print(type(li[2]))
print(type(li[3]))

#List slicing - similar to string slicing [::]
ebay_cart = [
  'books',
  'glasses',
  'pen',
  'orange'
]
ebay_cart[1] = 'laptop' #lists are mutable
print(ebay_cart[0:2])

# With new_list = my_list, you don't actually have two lists. The assignment just copies the reference to the list, not the actual list, so both new_list and my_list refer to the same list after the assignment 
#https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
#quickest way is to slice the list, but copy is also good
new_ebay_cart = ebay_cart[:]
new_ebay_cart_v2 = ebay_cart.copy

#Matrix
matrix1 = [
  [1,2,3],
  [2,3,4],
  [3,4,5]
]
print(matrix1 [1] [2]) #this will print the second column and third row in the matrix

#modifying list/adding to a list - all functions modify the list in question but do not create a new list.
list_v0 = [1,2,3,4,5]
list_v0.append(10)
list_v1 = list_v0[:]
list_v1.insert(2, 'inserted object')
list_v2 = list_v1[:]
list_v2.extend([20, 30, 40])
print(list_v2)

#removal of items in list
list_v2.pop(6) #removes last item or idexed item in bracket.
list_v2.remove(2) #removes first 2 which appears.
# list_v2.clear() #removes all items from the list
print(list_v2)

#additional list/array methods
print(list_v2.index('inserted object')) # returns index
print(30 in list_v2) #returns boolion - true or false
print(list_v2.count(5)) #returns how many times 5 is in list
#list_v2.sort() must contain only str or int
list_v3 = list_v2[:]
print(list_v3)

# Quick note a function starts at the begining and has a bracket e.g. function(object), a method is positioned after the object, e.g. object.method

# Another quick note, a function creats a new version of itself, so for sorted(list) to stick we must assign it a variable so new_list = sorted(list). A method on the other hand changes the list without creating a new one. So list.sort() will modify the list in all future code. Lets test this:

li = [1,2,3,4,2,3,4]
sorted(li)
print(li) #see this has not sorted so we now need:

li_new = sorted(li)
print(li_new) #now thats worked

#how about using the method rather than the function

li.sort()
print(li) #thats worked as well because ot stores the information

#say we want to put the numbers in reverse order. reverse simply flips the list so first we need to sort it.
li2 = [1,4,6,3,5,7,3,2,5,7,9]
li3 = li2[:]
li2.sort()
li2.reverse()
print(li2)

print(li3[::-1]) #another way to reverse (unsorted)

li4 = list(range(1, 20, 2)) #quick way to make a list
print(li4)

#make a list (can only contain str not int) into a string
li5 = ['1', '2', '3']
new_string = ' insert space here '.join(li5)
print(new_string)

#list unpacking
a,b,c, *other_var = [1,2,3,4,5,6,7,8,9]
print(b)
print(other_var)

#quick test - it worked
aa = 1
bb = 2
cc = 3
li7 = [aa,bb,cc]
print(li7)


# ------------------------------- DICTIONARY ----------------------------------

#Dictionary - a data structure like lists [a,b,c], dict is unordered key pairs, could be a username password pair. Values and keys can be any data type apart from keys can not be lists (keys can not be mutable). N.B./ kays are usually descriptive so they are strings.
my_dict = {
  'thwaitey':'password',
  'ceedee':2,
  'worrall': [1,3,2,6]
}

print(my_dict['worrall'])

#now we want to see if we have a certain user (key) in a dictionary

print(my_dict.get('hebe')) #specifies none if doesnt exist
print(my_dict.get('hebe', 999)) #999 if key doesnt exist

#boolean search for key only
print('password' in my_dict)

#dictionary methods - contains similar methods to lists
print('password' in my_dict.keys())
print('password' in my_dict.values())
print(my_dict.items())
my_dict2 = my_dict.copy()
print(my_dict2.clear())
my_dict.update({'ceedee': 'password2'})
print(my_dict)



# --------------------------------- TUPLES ------------------------------------

#tuple - like lists but imutable () rather than [] so canot sort or reverse, faster than lists though. So constants in tuples and variables in lists
xt,yt,*my_tuple = (1,2,3,4,5)
#my_tuple[1]= 5 #produces error message
print(my_tuple)

#only two specific tuple methods count and index + the generic methods such as len


# ---------------------------------- SETS -------------------------------------

#Set - unordered collection of unique objects {}
my_set = {1,2,3,4,5,5} # second 5 will not be returned
my_set.add(100)
print(my_set)

list_ex = [1,2,3,4,5,5,5,6]
set_ex = set(list_ex)
print(set_ex)
list_ex2 = list(set_ex)
print(list_ex2)

print(5 in my_set)

#set methods
my_set.difference(set_ex) #shows difference
my_set.discard(5) #discards defined value
my_set.difference_update(set_ex) #removes difference
my_set.intersection(set_ex) #common things so is 4,5,5
my_set.isdisjoint(set_ex) #anything in common boolean
my_set.union(set_ex) # joins set, removes dupliate | 
my_set.issubset(set_ex) #boolean is it a subset of set_ex
my_set.issuperset(set_ex) #boolean is it a superset of set_ex




# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')
