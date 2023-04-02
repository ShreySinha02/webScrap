import pandas as pd
import datetime

def saveCsv(data):
    dict={'id':[],'Heading':[],'URL':[],'Author':[],'Date':[]} 

    for i,d in enumerate(data):
        dict['id'].append(i+1)
        dict['Heading'].append(d[0])
        dict['URL'].append(d[1])
        dict['Author'].append(d[2])
        dict['Date'].append(d[3])
    df=pd.DataFrame(dict)
    filename = datetime.datetime.now().strftime("%d%m%Y") + "_verge.csv"
    df.to_csv(filename,index=False)
    return df
    