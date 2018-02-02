import datetime
import requests
import bs4 as bs
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter as xw
import openpyxl
import numpy as np


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
            if (otziv.find('div', class_='author') == None):
                cat = "None"
            else:
                category = otziv.find('div', class_='author')
                cat = category.find('span', class_='tag-mini mr10').text

            if (otziv.find('div', class_='office') == None):
                address = "None"
            else:
                address = otziv.find('div', class_='office').text
                address = address[20:]

            group.append(text)
            group.append(cat)
            group.append(address)
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
                if (otziv.find('div', class_='author') == None):
                    cat = "None"
                else:
                    category = otziv.find('div', class_='author')
                    cat = category.find('span', class_='tag-mini mr10').text

                if (otziv.find('div', class_='office') == None):
                    address = "None"
                else:
                    address = otziv.find('div', class_='office').text
                    address = address[20:]

                group.append(text)
                group.append(cat)
                group.append(address)
                elements.append(group)
            n = n + 1

        return elements

    def get_otziv_time():
        time = []
        URL = 'http://topbanki.ru/banks/sbrf/'
        response = requests.get(URL)
        soup = bs.BeautifulSoup(response.text, 'lxml')
        dates = soup.find_all(class_='actions')
        a = soup.find_all('ul', {'class': 'actions'})
        for el in a:
            data = el.text
            time.append(data)
            ##print(el.text)

        n = 2
        while n < 3:
            response = requests.get(URL + 'page' + str(n))
            soup = bs.BeautifulSoup(response.text, 'lxml')
            dates = soup.find_all(class_='actions')
            a = soup.find_all('ul', {'class': 'actions'})
            for el in a:
                data = el.text
                time.append(data)

            n = n + 1
        return time

    def get_right_time(time):
        now_date = datetime.date.today()
        now = now_date.strftime("%d %B %Y")
        delta = datetime.timedelta(days=1)
        yesterday_date = now_date - delta
        right_time = []
        for el in time:
            el = el.replace('Сегодня в', now)
            el = el.replace('Вчера в', yesterday_date.strftime("%d %B %Y"))
            el = el.replace('January', 'января')
            el = el.replace('February', 'февраля')
            el = el.replace('March', 'марта')
            el = el.replace('April', 'апреля')
            el = el.replace('May', 'мая')
            el = el.replace('June', 'июня')
            el = el.replace('July', 'июля')
            el = el.replace('August', 'августа')
            el = el.replace('September', 'сентября')
            el = el.replace('October', 'октября')
            el = el.replace('November', 'ноября')
            el = el.replace('December', 'декабря')
            right_time.append(el)
        return right_time

    def export_to_excel(otzivi, right_time):
        df = pd.DataFrame(otzivi)
        df.index = right_time
        df.columns = ['Текст Отзыва', 'Категория', 'Адрес офиса']
        df.index.names = ['Дата']
        # print(df)
        writer = ExcelWriter('TopBanks.xlsx')
        df.to_excel(writer, 'Feedbacks')
        writer.save()

        wb = openpyxl.load_workbook('TopBanks.xlsx')
        ws = wb.get_sheet_by_name('Feedbacks')
        dims = {}
        for row in ws.rows:
            for cell in row:
                if cell.value:
                    dims[cell.column] = max((dims.get(cell.column, 0), len(cell.value)))
        for col, value in dims.items():
            # value * коэфициент
            ws.column_dimensions[col].width = value * 1.5

        wb.save("TopBanks.xlsx")

    otzivi = get_otziv_info()
    time = get_otziv_time()
    right_time = get_right_time(time)
    final_otzivi = export_to_excel(otzivi, right_time)