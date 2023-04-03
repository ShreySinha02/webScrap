from flask import Flask,render_template,url_for
from webScrap import Scrapper
from saveCsv import saveCsv
from sqlcon import sqlCon

app = Flask(__name__)
url="https://www.theverge.com/"
@app.route('/')
def index():
    data=Scrapper(url)
    verge=saveCsv(data)
    return render_template('index.html',verge=verge)


if __name__=='__main__':
    app.run(debug=True)
   
    
   
   
   
   
   
   
   
   
   
   

#  
#     # scrap the website
#     data=Scrapper(url)
#     print(data)
#     # save the data in csv file 
#     saveCsv(data)
    
#     # connect the data in sqllite
#     sqlCon(data)
