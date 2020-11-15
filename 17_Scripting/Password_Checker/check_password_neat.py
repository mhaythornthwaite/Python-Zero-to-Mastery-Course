# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:42:05 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#------------------------------ PASSWORD CHECKER ------------------------------


import requests
import hashlib



#takes the first 5 charaters of the hashed password and returns the API response from pwned passwords (class: requests.models.Response)

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error {res.status_code}')
    return res



#takes the password, converts into sha1 hash, and sends the first 5 characters to the pwned API. Pwned API returns the tails (last 35 charaters) of every password matching the intial 5 charaters of the input password. This is returned as a string with the addition of the number of times hacked appended to each hash.

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))    
    first_5_char = (sha1password.hexdigest())[0:5]
    response = request_api_data(first_5_char).text
    return response



#Converts the password into sha1 hash and then returns the tail (last 35 characters)

def password_hash_tail(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))
    tail_l = (sha1password.hexdigest())[5:]
    tail_u = tail_l.upper()
    return tail_u



#processing the string provided by pwned, into a list in the format of [hash, times hacked, hash, times hacked, ...]

def pwned_api_str_to_li(pwned_data):
    raw_hash_list = pwned_data.split(':')
    proc_hash_list = []
    for i in raw_hash_list:
        mini_li = i.split('\r\n')
        for j in mini_li:
            proc_hash_list.append(j)
    return proc_hash_list
     


#takes the hash tail of the password in question and compares against pwned list. If a match is found, this data will be printed. If no match is found this this also printed.
    
def password_check(password_hash_tail, pwned_api_list):
    count = 0
    for x in pwned_api_list:
        if x == password_hash_tail:
            location = int(pwned_api_list.index(x)) + 1
            times_hacked = pwned_api_list[location]
            print(f'\n***************************************************************\nYour password has been hacked {times_hacked} times, consider changing it!\n***************************************************************\n')
        else:
            count = count + 1
        if count == len(pwned_api_list):
            print('\n*********************************************\nYour password has never been hacked, nice one!\n*********************************************\n')
            
     
        
#executing the above functions.    
        
password = str(input('What\'s your password? '))
            
password_hash_string_data = pwned_api_check(password) 

password_hash_list_data = pwned_api_str_to_li(password_hash_string_data)

pass_hash_tail = password_hash_tail(password)

password_check(pass_hash_tail, password_hash_list_data)




# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')