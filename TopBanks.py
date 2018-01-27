import requests
import bs4 as bs
import pandas as pd
import numpy as np
from openpyxl import Workbook


def get_otziv_info():
    URL = 'http://topbanki.ru/banks/sbrf/'
    response = requests.get(URL)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    otziv_text = soup.find_all('p')
    # print(len(otziv_text))
    otziv_text = otziv_text[1:-2]
    n = 2
    while n < 4:
        response = requests.get(URL + 'page' + str(n))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        otziv_text1 = soup.find_all('p')
        otziv_text1 = otziv_text1[:-2]
        for el in otziv_text1:
            otziv_text.append(el)

        n = n + 1

    return otziv_text

a = get_otziv_info()
#print(a)

def get_otziv_time():
    otziv_data = []
    URL = 'http://topbanki.ru/banks/sbrf/'
    response = requests.get(URL)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    dates = soup.find_all(class_='actions')
    a = soup.find_all('ul', {'class': 'actions'})
    for el in a:
        data = el.text
        otziv_data.append(data)
        ##print(el.text)

    n = 2
    while n < 4:
        response = requests.get(URL + 'page' + str(n))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        dates = soup.find_all(class_='actions')
        a = soup.find_all('ul', {'class': 'actions'})
        for el in a:
            data = el.text
            otziv_data.append(data)

        n = n + 1
    return otziv_data
b = get_otziv_time()
#print(b)

data = {'text': get_otziv_info()}

df = pd.DataFrame(data)
df.index = get_otziv_time()
#print(df)

def get_otziv_category():
    URL = 'http://topbanki.ru/banks/sbrf/'
    count = 0
    response = requests.get(URL)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    otziv_category = []
    a = soup.find_all('span', class_='tag-mini mr10')
    for el in a:
        category = el.text
        otziv_category.append(category)
        count = count + 1

    n = 2
    while n < 4:
        response = requests.get(URL + 'page' + str(n))
        soup = bs.BeautifulSoup(response.text, 'lxml')
        a = soup.find_all('span', class_='tag-mini mr10')
        for el in a:
            category = el.text
            otziv_category.append(category)
            count = count + 1

        n = n + 1

    return otziv_category, count


c = get_otziv_category()
#print(c)