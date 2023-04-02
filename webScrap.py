from bs4 import BeautifulSoup
import requests
import re

def Scrapper(url):
     #sucess code
    r= requests.get(url)
    #parsing the html

    soup=BeautifulSoup(r.content,'html.parser')
    root =soup.find('div',id='__next')

    head=root.find_all('h2')

    data=[]
    for h in head:
        author=h.find_next_sibling('div',class_='relative')
        if author != None:
            link=h.find('a')
            auth=author.find('a').get_text()
            span=author.find('span').get_text()
            data.append([link.text,link.get('href'),auth,span])
            # print(link.get('href'),auth,span)
    return data
    