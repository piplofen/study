import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://leroymerlin.ru/catalogue/dreli-shurupoverty/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
'accept': '*/*'}
HOST = 'https://leroymerlin.ru'
FILE = 'Lerua.csv'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_pages_count(html):
	soup = BeautifulSoup(html, 'html.parser')
	pagenation = soup.find_all("a", class_ = "bex6mjh_plp o1ojzgcq_plp l7pdtbg_plp r1yi03lb_plp sj1tk7s_plp")
	if pagenation:
		return int(pagenation[-1].get_text())
	else:
		return 1

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all("div", class_ = "phytpj4_plp largeCard")

	lerua = []

	for item in items:
		purchase = item.find("span", class_ = "cef202m_plp").find("span", class_ = "t3y6ha_plp s1dis8vt_plp l1tt5nnx_plp p105rlqh_plp blue")
		if purchase:
			purchase = purchase.text
		else:
			purchase = "Онлайн и оффлайн"

		name = item.find("a", class_ = "bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp").get("aria-label")
		if "м²" in name:
			name = name.replace("м²", "м2")
			name = name.replace("\u200e", "")

		lerua.append({
			"name": name,
			"link": HOST + item.find("a", class_ = "bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp").get("href"),
			"price": item.find("p", class_ = "t3y6ha_plp xc1n09g_plp p1q9hgmc_plp").get_text().strip(""),
			"purchase": purchase
			})
	return lerua

def save_file(items, path):
	with open(path, "w", newline = "") as file:
		writer = csv.writer(file, delimiter = ";")
		writer.writerow(["Название","Ссылка","Цена","Способ покупки"])
		for item in items:
			writer.writerow([item["name"],item["link"],item["price"],item["purchase"]])

def parse():
	URL = input("Введите URL: ")
	URL = URL.strip()
	#if URL == "Отвертки":
		#URL = "https://kaliningrad.leroymerlin.ru/catalogue/otvertki/"
	html = get_html(URL)
	print(html.status_code)
	if html.status_code == 401:
		lerua = []
		pages_count = get_pages_count(html.text)
		for page in range(1, pages_count + 1):
			print(f"Парсиннг страницы {page} из {pages_count}.")
			html = get_html(URL, params = {"page": page})
			lerua.extend(get_content(html.text))
		save_file(lerua, FILE)
		print(f"Получено {len(lerua)} элементов.")
		os.startfile(FILE)
	else:
		print("Error")

parse()
