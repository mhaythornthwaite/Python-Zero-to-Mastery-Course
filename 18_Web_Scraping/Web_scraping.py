# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:39:09 2020

@author: mhayt
"""


print('\n\n')
print(' ---------------- START ---------------- ')

#-------------------------------- WEB SCRAPING --------------------------------

#to find out what the website is happy for you to scrape, you simply type /robots.txt 
#this simply states what the website is happy for you to take, but practically you can take anything.
#the listed items are simply the extensions to the webpage.
#note on the hacker news there is a requested 'crawl delay' of 30 seconds, this means you should request information from the web page more than every 30 seconds, as this adds traffic and ultimately could crash their servers.

#easiest way to get data from a website is from an API (Applicastion Programming Interface). It is effectively just a list of information that is stored and often used by a website or piece of software. (So far the data appears to be arranged in a kind of dictionary.)

#----- SWAPI API -----

#Just searched the star wars API which provides a list of all the characters in star wars with the following link in HTTPS:
#https://swapi.co/api/people/


#----- JSON API -----

#This api provides simples data like photos that we can use for building a website or test ML code (in JSON format).
#https://jsonplaceholder.typicode.com/photos


#----- SEARCH ENGIONE OPTIMISATION SEO -----

#google and other search engines originally started by crawling every website and looking for what the user has searched, if it appears in the website it will appear in the list provided. So search engines are constantly crawling websites for data, which is effectively what we want to do with web scraping.(n.b./ googlebot is what google uses to crawl.) 


#-------------------------- WEB SCRAPING HACKER NEWS --------------------------

#we're going to web scrape using the beautiful soup library.


import requests as rq
from bs4 import BeautifulSoup as bs

#requesting the url and testing to see a good response <Response [200]>
response = rq.get('https://news.ycombinator.com/news')
print(response)

#go to developer tools in the website, open netwrok, refresh, this is what we're requesting.
#print(response.text)

#we can use beautiful soup to turn the string into an object. Note we have to define html.parser, as beautifulsoup also does xml. 
soup = bs(response.text, 'html.parser')
print(type(soup), '\n')
print(soup.title)
print(soup.head)

#Additional find methods
'''
print(soup.body.contents)`
print(soup.find_all('div')) #find all the div objects
print(soup.find_all('a')) #find all the a tags which are all the links
print(soup.a) #first a tag
print(soup.find('a')) #finds the first item
'''

#id found with the inspector. The inspector is really going to become useful for findng unique identfiers of the specific data we're after.
print('\n', soup.find(id='score_22644983'))


soup.select('.score') #selects all the classes of score (. stands for a class)
soup.select('#score_22644983') #selects all the id's (# stands for a id)


links = soup.select('.storylink')
votes = soup.select('.score')


print('\n', links[0], votes[0])

print(len(links))
print(votes[0].getText())


#removes characters in a string so only digits are left

def remove_char(input_string):
    oput = ''.join(i for i in input_string if i.isdigit())
    return oput
    

#iterates over list of links and votes. If the number of votes are > 100 then something is appended to the hn list

def create_custom_hn(links, votes):
    hn = []
    l_links = len(links)
    for x in range(l_links):
        vote_dig_s = remove_char(votes[x].getText())
        vote_dig = int(vote_dig_s)
        link = links[x].get('href', None)
        title = links[x].getText()
        if vote_dig > 99:
            hn.append({'title': title, 'link': link, 'number_of_votes': vote_dig})
    return hn


#create the list
top_rated_list = create_custom_hn(links, votes)


#this list is effectively a list of dictionaries, each with only 3 keys: title, key and #votes. Now to print the list to make it more readable

def print_with_spaces(input_list):
    for x in range(len(input_list)):
        print(input_list[x], '\n')
        
#print_with_spaces(top_rated_list)

print(top_rated_list[0]['number_of_votes'])



#----- MAKING THINGS LOOK NICE -----

# =============================================================================
# hmm actually thing mine looks better
# 
# import pprint
# 
# pprint.pprint(top_rated_list)
# =============================================================================


def ordering_list(input_list):
    return sorted(input_list, key = lambda k:k['number_of_votes'], reverse = True)

top_rated_list_ordered = ordering_list(top_rated_list)
#print_with_spaces(top_rated_list_ordered)



#---------------------- HACKER NEWS SECOND PAGE EXERCISE ----------------------


#attaining the second page response
response2 = rq.get('https://news.ycombinator.com/news?p=2')


#making the response a beautifulsoup object
soup2 = bs(response2.text, 'html.parser')


#creating the links and the votes
links2 = soup2.select('.storylink')
votes2 = soup2.select('.score')


#creating the list with the create_custom_hn function
top_rated_list_p2 = create_custom_hn(links2, votes2)


#attaching page 1 to page 2
top_rated_list_p1p2 = top_rated_list + top_rated_list_p2


#ordering the combined pages
top_rated_list_ordered_p1p2 = ordering_list(top_rated_list_p1p2)


#printing the ordered combined pages
print_with_spaces(top_rated_list_ordered_p1p2)







print('\n', '----------BETFAIR WORKING AREA----------', '\n')
#------------------------------ BETFAIR TEST AREA -----------------------------

r = rq.get('https://www.betfair.com/sport/football/belarussian-premier-league/vitebsk-v-gorodeya/29754573')
print(r)

r = rq.get('https://www.betfair.com/sport/home')
print(r)


#use the inspector to find the data locations we are after, we can then use this to better search in our scraped html file. 
#<a href="/sport/football/belarussian-premier-league/vitebsk-v-gorodeya/29754573?action=openDataVisualizationMStats&amp;modules=matchheader" class="matchheader-tab matchheader-anchor ui-nav btn-pitch-view-mstats selected" data-loader=".matchheader-tabs-content" id="yui_3_5_0_1_1584791359515_163558"> Match Stats </a>

r = rq.get('https://www.betfair.com/sport/football/friendly-matches/ifk-stocksund-v-karlbergs-bk/29757987')
s = bs(r.text, 'html.parser')
r_txt = str(r.raw)
s_str = str(s)
print(s)
#print(s.select('.draw'))
print(s.find_all('.mod-subheader-component-value ui-subheader-value'))
print(s.findAll("div", {"class": "ui-football-statistics-entities-FootballStatistics-HomeAttacks"}))
print(s.select('football-statistics'))
#print(s.text)

#seems as though betfair block this live data from being accessed via requests. Might need a different method for scraping betfair data. Their API's are only available for exchange and arcade games


with open('test', mode='w') as my_file:
	text = my_file.write(r_txt)




# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')