# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:15:58 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#------------------------------ PASSWORD CHECKER ------------------------------


import requests
import hashlib

#password api url:

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)

#response 400 usually means not authorised, 200 is what we want.
print(res)

#we should never store a users password in plain text it should be hashed. Hashing is non stochastic and also a one way function. The below is the same code but with 'password123' hashed with SHA1


url = 'https://api.pwnedpasswords.com/range/' + 'cbfdac6008f9cab4083784cbd1874f76618d2a97'
res = requests.get(url)
print(res)


#still not secure though because we could write a function that converts every single password possible to SHA1 hash and then we have found the password.
#so big companies use k-anonymity > this is using only the first 5 digits of the hashed password

url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'
res = requests.get(url)
print(res)


#so in the above we are requesting all the hashed passwords that begin with the first 5 digits, this will be a lot and then we can work locally on these rather than requesting a single password. Therefore the pwned API will not know the requested password only a range of passwords.


#lets create a function thats going to request our data and give us a response



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error {res.status_code}')
    return res


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))
    
    #print('\n', sha1password) #hash object
    #print(sha1password.hexdigest(), '\n') #outputs sha1 hash
    
    first_5_char = (sha1password.hexdigest())[0:5]
    response = request_api_data(first_5_char).text
    return response



def password_hash_tail(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))
    tail_l = (sha1password.hexdigest())[5:]
    tail_u = tail_l.upper()
    return tail_u



def pwned_api_str_to_li(pwned_data):
    raw_hash_list = pwned_data.split(':')
    
    proc_hash_list = []
    
    for i in raw_hash_list:
        mini_li = i.split('\r\n')
        for j in mini_li:
            proc_hash_list.append(j)
    
    return proc_hash_list
     
    
def password_check(password_hash_tail, pwned_api_list):
    count = 0
    for x in pwned_api_list:
        if x == password_hash_tail:
            location = int(pwned_api_list.index(x)) + 1
            times_hacked = pwned_api_list[location]
            print(f'\n***************************************************************\nYour password has been hacked {times_hacked} times, consider changing it\n***************************************************************\n')
        else:
            count = count + 1
        if count == len(pwned_api_list):
            print('\n*********************************************\nYour password has never been hacked, nice one\n*********************************************\n')
            
     
        
password = str(input('whats your password? '))
            
password_hash_string_data = pwned_api_check(password) 

password_hash_list_data = pwned_api_str_to_li(password_hash_string_data)

pass_hash_tail = password_hash_tail(password)

password_check(pass_hash_tail, password_hash_list_data)





'''
SMALL TEST CODE SNIPET TO CREAT LIST
  
test_st = ['aa11aab', 'zz11zzb']   
output = []

for i in test_st:
    x = i.split('11')
    for j in x:
        output.append(j)

print(output)

'''

# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
