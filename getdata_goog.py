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
        url = 'https://google.com/search?q=' + stockname
        r = requests.get(url, headers=header)
        self.soups = BS(r.text, features="html.parser")

    def getprice(self):
        self.lastprice = self.soups.find("span", {"class": "IsqQVc NprOob XcVN5d"}).text
        return self.lastprice

    def arrayify(self):
        testarray = np.array ([[self.stockname],[self.lastprice]])
        return testarray


summary = [[],[]]
temp_array=0

stocklist = np.array((['MSFT','AAPL','CRWD','TSLA'],[1,2,1,0]))

for i in stocklist[0]:
    stock = Stock(i)
    stock.getprice()
    temp_array=stock.arrayify()
    summary = np.hstack((summary, temp_array))

print(summary)

