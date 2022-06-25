import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://stv39.ru/catalog/lampy_galogennye/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
'accept': '*/*'}
HOST = 'https://stv39.ru'
FILE = 'light.csv'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_pages_count(html):
	soup = BeautifulSoup(html, 'html.parser')
	pagenation = soup.find("ul", class_ = "pagination")
	if pagenation:
		print(pagenation.get_text().strip()[-2:])
		return int(pagenation.get_text().strip()[-2:])
	else:
		print(1)
		return 1

def save_file(items, path):
	with open(path, "w", newline = "") as file:
		writer = csv.writer(file, delimiter = ";")
		writer.writerow(["Название","Ссылка","Цена","Количество"])
		for item in items:
			writer.writerow([item["name"],item["link"],item["price"],item["purchase"]])

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all("div", class_ = "cell product-cell")
	#print(items)

	light = []

	for item in items:
		light.append({
			"name": item.find("a", class_ = "prod__title").get_text().strip(),
			"link": HOST + item.find("a", class_ = "prod__title").get("href"),
			"price": item.find("div", class_ = "shrink cell").get_text().strip(),
			"purchase": item.find("div", class_ = "prod__av").get_text().strip()
			})
	return light

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		light = []
		pages_count = get_pages_count(html.text)
		for page in range(1, pages_count + 1):
			print(f"Парсинг страницы {page} из {pages_count}")
			html = get_html(URL, params = {"disable_ajax=N&PAGEN_1": page})
			light.extend(get_content(html.text))
		save_file(light, FILE)
		print(f"Получено {len(light)} элементов.")
		os.startfile(FILE)

parse()