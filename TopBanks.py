import requests
import bs4 as bs
import pandas as pd
import numpy as np
from openpyxl import Workbook


class TopBanks:
    def get_otziv_info():
        elements = []
        URL = 'http://topbanki.ru/banks/sbrf/'
        response = requests.get(URL)
        soup = bs.BeautifulSoup(response.text, 'lxml')
        otziv_group = soup.find_all('div', class_='response_table__data')
        for otziv in otziv_group:
            group = []
            text = otziv.find('p').text
            #time = otziv.find('li').text
            if (otziv.find('div', class_='office') == None):
                office = "-"
            else:
                office1 = otziv.find('div', class_='office')
                office = office1.find(class_='mr10').text

            if (otziv.find('div', class_='author') == None):
                cat = "-"
            else:
                category = otziv.find('div', class_='author')
                cat = category.find('span', class_='tag-mini mr10').text
            group.append(text)
            #group.append(time)
            group.append(office)
            group.append(cat)
            elements.append(group)

        n = 2
        while n < 3:
            URL = 'http://topbanki.ru/banks/sbrf/'
            response = requests.get(URL + 'page' + str(n))
            soup = bs.BeautifulSoup(response.text, 'lxml')
            otziv_group = soup.find_all('div', class_='response_table__data')
            for otziv in otziv_group:
                group = []
                text = otziv.find('p').text
                #time = otziv.find('li').text
                if (otziv.find('div', class_='office') == None):
                    office = "-"
                else:
                    office1 = otziv.find('div', class_='office')
                    office = office1.find(class_='mr10').text

                if (otziv.find('div', class_='author') == None):
                    cat = "-"
                else:
                    category = otziv.find('div', class_='author')
                    cat = category.find('span', class_='tag-mini mr10').text
                group.append(text)
                #group.append(time)
                group.append(office)
                group.append(cat)
                elements.append(group)
            n = n + 1

        return elements

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
        while n < 3:
            response = requests.get(URL + 'page' + str(n))
            soup = bs.BeautifulSoup(response.text, 'lxml')
            dates = soup.find_all(class_='actions')
            a = soup.find_all('ul', {'class': 'actions'})
            for el in a:
                data = el.text
                otziv_data.append(data)

            n = n + 1

        return otziv_data

    time = get_otziv_time()
    elements = get_otziv_info()

    #data = {'text': get_otziv_info()}

    df = pd.DataFrame(elements)
    df.index = get_otziv_time()
    print(df)