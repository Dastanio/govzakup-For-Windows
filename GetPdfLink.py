#Парсер2
from bs4 import BeautifulSoup
import requests
import urllib3
import re

AdsIndex = str(input('Введите номер обьявление: '))

result = []
info = []

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('https://goszakup.gov.kz/ru/announce/index/' + AdsIndex +'?tab=documents', verify=False)
soup = BeautifulSoup(response.text, 'html.parser')
item = soup.find('div', class_ = 'panel-body').find_all('div', class_='col-sm-7')

#тут храниться все данные 
for i in item:
	info.append(i.find('input', class_ = 'form-control').get('value'))


items = soup.find('table', class_='table table-bordered table-hover table-striped').findAll('button')

for i in items:
	data_file = re.findall(r'actionModalShowFiles(.+,.+);', i.attrs['onclick'])[0][1:-1]
	idAnno = data_file.split(',')[0]
	idGroup = data_file.split(',')[1]
	link = 'https://goszakup.gov.kz/ru/announce/actionAjaxModalShowFiles/{}/{}'.format(idAnno, idGroup)

	response2 = requests.get(link, verify=False)
	soup2 = BeautifulSoup(response2.text, 'html.parser')

	link_doc = soup2.findAll('a')

	if link_doc != []:
		result.append(link_doc[0].attrs['href'])
	else:
		print(None)
