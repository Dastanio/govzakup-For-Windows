import fitz
import re
import requests
import urllib3
from GetPdfLink import result, info
import pathlib
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class PDF:
    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.pdfObject = fitz.open(pathFile)
    #Поиск ключевого слова в определенной странице, idpage - страница, pattern - ключевое слово 
    def findPage(self, idPage, pattern):
        currentPage = self.pdfObject.loadPage(idPage)
        textCurrentPage = currentPage.getText()
        if re.search(pattern, textCurrentPage):
            return (True, textCurrentPage)
        else:
            return (False, None)

    #Поиск по слову если оно есть во всех страницах пдф, то добовляет в список=[Номер страницы, содиржимое страницы]
    def findAllPage(self, pattern):#pattern - поиск 
        results = []
        for idPage in range(self.pdfObject.pageCount):
            currentPage = self.pdfObject.loadPage(idPage)
            textCurrentPage = currentPage.getText()
            if re.search(pattern, textCurrentPage):
                results.append(('На странице номер', idPage+1, 'нашлость ключевое слово: ',pattern))
        return results

filename = 'Итого'
keywords = input('Введите ключевое слово: ')


number_pdf = 0
nameads = info[1][:100]
nameads = nameads.replace('"', '')
os.mkdir(nameads)


namefile = str(filename) + '.txt'

with open(os.path.join(nameads, namefile), 'a') as f:
    f.write('\n')
    f.write('Номер объявления: ' + info[0])
    f.write('\n')
    f.write('Наименование объявления: ' + info[1])
    f.write('\n')
    f.write('Статус объявления: ' + info[2])
    f.write('\n')
    f.write('Дата публикации объявления: ' + info[3])
    f.write('\n')
    f.write('Срок начала приема заявок: ' + info[4])
    f.write('\n')
    f.write('Срок окончания приема заявок: ' + info[5])
    f.write('\n')


for link_doc in result:
    response = requests.get(link_doc, verify=False)

    pdfname = 'pdf_'+str(number_pdf)+'.pdf'
    
    with open(os.path.join(nameads, pdfname), 'wb') as f:
        f.write(response.content)

    number_pdf += 1

    pdf = PDF(os.path.join(nameads) + '\\' + pdfname)
    alltext = pdf.findAllPage(keywords)
    namefile = str(filename) + '.txt'
    for i in alltext:  
        with open(os.path.join(nameads, namefile), 'a') as f:
            f.write('\n')
            f.write(str(i)+ ' В документе ' + pdfname)
            f.write('\n')