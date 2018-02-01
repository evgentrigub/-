import requests
import bs4 as bs
from openpyxl import Workbook

class IRecommend:
    def get_otziv_link():
        URL = 'http://irecommend.ru'
        otziv_links = []
        count = 0
        response = requests.get('http://irecommend.ru/content/sberbank?new=1')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        otzivi_group = soup.find_all('div', class_='nobr')
        for otziv_link in otzivi_group:
            for link in otziv_link.find_all('a'):
                otziv_links.append(URL + link['href'])
                count = count + 1
        print(count)

        return otziv_links


    links = get_otziv_link()
    print(links)

