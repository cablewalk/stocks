from bs4 import BeautifulSoup as BS
import urllib
import re
import urllib.request
import requests
import re
import numpy as np

class Stock:
    def __init__(self, stockname):
        self.stockname = stockname.split(' ',1)[0] #removes characters following a space
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
        url = 'https://google.com/search?q=' + stockname
        r = requests.get(url, headers=header)
        self.soups = BS(r.text, features="html.parser")

    def getprice(self):
        try: 
            self.lastprice = self.soups.find("span", {"class": "IsqQVc NprOob XcVN5d"}).text
            self.lastprice = self.lastprice.replace(',', '')
        except AttributeError as e:
            self.lastprice = 0
            return self.lastprice
        return float(self.lastprice)

    def arrayify(self):
        testarray = np.array ([[self.stockname],[self.lastprice]])
        return testarray


summary = [[],[]]
temp_array=0
portfolio = 0

stocklist = np.array((['MSFT','AAPL','CRWD','XLK','LIT stock', 'PRNT stock','QQQ'],[1,2,1,2,10, 12,2]))

for i in stocklist[0]:
    stock = Stock(i)
    stock.getprice()
    temp_array=stock.arrayify()
    summary = np.hstack((summary, temp_array))

print(summary)

ownnums = np.array(stocklist[1], dtype=float) #dtype conversion to float for array multiplication
pricelist = np.array(summary[1], dtype=float)

portfolio = np.multiply(pricelist, ownnums)   #list consisting of prices of stocks i own

print(sum(portfolio))


