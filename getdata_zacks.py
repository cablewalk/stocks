from bs4 import BeautifulSoup as BS
import urllib
import re
import urllib.request
import requests
import re
import numpy as np

class Stock:
    def __init__(self, stockname):
        self.stockname = stockname
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
        url = 'https://www.zacks.com/stock/quote/' + stockname
        r = requests.get(url, headers=header)
        self.soups = BS(r.text, features="html.parser")
        

    def getprice(self):
        lastprice = self.soups.find("p", {"class": "last_price"}).text
        self.lastprice = ''.join(re.findall(r"^(.*)....$", lastprice))
        return self.lastprice

    def zacksrating(self):
        rating = self.soups.find("p", {"class": "rank_view"}).text
        self.rating = ''.join(re.findall(r"1-Strong Buy|2-Buy|3-Hold|4-Sell|5-Strong Sell", rating))
        
        return self.rating
        
    def arrayify(self):
        testarray = np.array ([[self.stockname],[self.lastprice],[self.rating]])
        return testarray



stocklist = np.array(['MSFT','AAPL','CRWD','TSLA'])

summary = [[],[],[]]
temp_array=0

for i in stocklist:
    stock = Stock(i)
    stock.getprice()
    stock.zacksrating()
    temp_array=stock.arrayify()
    summary = np.hstack((summary, temp_array))

print(summary)

