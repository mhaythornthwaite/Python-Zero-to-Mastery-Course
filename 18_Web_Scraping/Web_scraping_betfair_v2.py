# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:49:40 2020

@author: mhayt
"""



print('\n\n')
print(' ---------------- START ---------------- ')


#------------------------------ BETFAIR TEST AREA -----------------------------


import requests as rq
from bs4 import BeautifulSoup as bs


r = rq.get('https://www.betfair.com/sport/football/friendly-matches/eskilsminne-v-angelholms/29759915')
s = bs(r.text, 'html.parser')

#print(s.select('.draw'))

print(s.find_all('.mod-subheader-component-value ui-subheader-value'))
print(s.findAll("div", {"class": "ui-football-statistics-entities-FootballStatistics-HomeAttacks"}))

print(s.select('.bg-pager'))

print(s.select('.football-statistics'))


print(s.findAll("div", {"class": "football-statistics"}))

print(s.findAll("div", {"class": "bg-pager-page bg-pager-page-0"}))

print(s.findAll("span", {"class": "ui-football-statistics-entities-FootballStatistics-HomeTotalShots"}))

print(s.findAll("div", {"class": "matchheader-tabs ui-inplay ui-has-score ui-event ui-29759915 "}))

print(s.findAll("data-bindings", {"class": "ui_football_statistics_entities_FootballStatistics.HomeTotalShots"})) #not worked

# print(s.select('.grid-1')) #that worked




#print(s.text)

#seems as though betfair block this live data from being accessed via requests. Might need a different method for scraping betfair data. Their API's are only available for exchange and arcade games


# =============================================================================
# 
# r_txt = str(r.raw)
# s_str = str(s)
# 
# with open('test.txt', mode='w') as my_file:
# 	text = my_file.write(s_str)
# 
# =============================================================================




import requests
from bs4 import BeautifulSoup
 
url = "https://www.betfair.com/sport/football/friendly-matches/eskilsminne-v-angelholms/29759915"
url_get = requests.get(url)
soup = BeautifulSoup(url_get.content, 'lxml')
 
with open('url.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(soup.prettify())




# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')

