#Парсер 1
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://goszakup.gov.kz/ru/search/announce'
HOST = 'https://goszakup.gov.kz'

def get_html(URL, params = ''):
    r = requests.get(url, params=params, verify=False)
    url2 = r.url
    return str(url2)

def get_html2(secondURL, params = ''):
    r2 = requests.get(secondURL,params, verify = False)
    return r2

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.select("tbody a")
    cards = []

    for item in items:
        cards.append(
            {
                'link': HOST + item.attrs['href']
            }
        )
    
    return cards


def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())

    search = input('Название обьявление: ')

    html = get_html(url, params={'filter[name]':str(search)})
    html2 = get_html2(html)
    if html2.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html2 = get_html2(html, params={'page': page})
            cards.extend(get_content(html2))
        #print(cards)
        pass
    else:
        print('Error')
    for i in cards:
        print(i['link'].split('/')[-1])
parser()
