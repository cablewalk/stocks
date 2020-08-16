from bs4 import BeautifulSoup as BS
import urllib
import re
import urllib.request
import requests
import re

class Stock:
    def __init__(self, input_url):
        self.input_url = 'https://www.zacks.com/stock/quote/' + input_url
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
        url = self.input_url
        r = requests.get(url, headers=header)
        self.soups = BS(r.text, features="html.parser")
        print(input_url.upper())
        

    def getprice(self):
        lastprice = self.soups.find("p", {"class": "last_price"}).text
        lastprice = re.findall(r"^(.*)....$", lastprice)
        
        return lastprice

    def zacksrating(self):
        rating = self.soups.find("p", {"class": "rank_view"}).text
        rating = re.findall(r"1-Strong Buy|2-Buy|3-Hold|4-Sell|5-Strong Sell", rating)
        
        return rating

a = Stock('AAPL')
print(a.getprice())
print(a.zacksrating())
stockinput = input()

b = Stock(stockinput)
print(b.getprice())
print(b.zacksrating())