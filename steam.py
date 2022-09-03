import requests
import time
import datetime
from bs4 import BeautifulSoup


url = input('Paste the item link( default is ghost town sniper rifle): ')
if url == '':
    url = 'https://steamcommunity.com/market/search?q=ghost+town&category_440_Collection%5B%5D=any&category_440_Type%5B%5D=tag_primary&category_440_Class%5B%5D=tag_Sniper&category_440_Quality%5B%5D=tag_strange&appid=440'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
tags = soup('a')

def find():
    if soup.find_all('a', id="resultlink_0"):
        dat = soup.find_all('a', id="resultlink_0")
        for x in dat:
            d = x.get('href', None)
            z = x.find('span',  class_="sale_price").text
            g = x.find('span', id="result_0_name").text
            print('\n','Item ',g,'is currently on sale for: ', z)
            print('\a')
            time.sleep(1)
            print('\a')
            exit()
    else:
        print('Currently not on sale')

if __name__ == '__main__':
    while True:
        find()
        x = datetime.datetime.now()
        print(x.strftime("%c"), "\n")
        time.sleep(60)