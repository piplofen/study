import requests
from bs4 import BeautifulSoup as BS

urlKGD = "https://kgd.ru/pogoda/1-pogoda-v-kaliningrade"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
'accept': '*/*'}

weather = []

def get_html(url):
    r = requests.get(url, headers = HEADERS)
    return r

def get_content(html):
    soup = BS(html, "html.parser")
    temp = soup.find("div", class_ = "current_weather").find("div", class_ = "temp").text
    additional = soup.find_all("div", class_ = "rhs")

    for i in range(len(additional)):
        weather.append({
            "temp": temp,
            "wind": additional[0].text,
            "humidity": additional[1].text,
            "pressure": additional[2].text,
            "cloudiness": additional[3].text,
            "visibility": additional[4].text
        })

def parse(url):
    html = get_html(url)
    if html.status_code == 200:
        get_content(html.text)
    return weather

if __name__ == '__main__':
    parse(urlKGD)