import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://baucenter.ru/ekrany_dlya_vann_universalnye/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
'accept': '*/*'}
HOST = 'https://baucenter.ru'
FILE = 'Baucenter.csv'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_pages_count(html):
	soup = BeautifulSoup(html, 'html.parser')
	pagenation = soup.find_all("a", class_ = "hidden-xs pagination_button")
	#print(pagenation)

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all("div", class_ = "catalog_item with-tooltip")

	baucenter = []

	for item in items:
		baucenter.append({
			"name": item.find("div", class_ = "catalog_item_heading h4").get_text().strip(),
			"link": HOST + str(item.find("a").get("href")),
			"price": item.find("span", class_ = "price-block_price yellow-price").get_text().strip().replace(" ", "").replace(".–зашт", " руб.")
			})

	print(baucenter)
	return baucenter

def parse():
	html = get_html(URL)
	get_content(html.text)
	get_pages_count(html.text)

parse()