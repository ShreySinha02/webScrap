
from webScrap import Scrapper
from saveCsv import saveCsv
from sqlcon import sqlCon

if __name__=='__main__':
    url="https://www.theverge.com/"
    # scrap the website
    data=Scrapper(url)
    print(data)
    # save the data in csv file 
    saveCsv(data)
    
    # connect the data in sqllite
    sqlCon(data)
    
   