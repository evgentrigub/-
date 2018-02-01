import requests
import bs4 as bs
from openpyxl import Workbook

class Otzovik:
    def get_otziv_link():
        otziv_links = []
        count = 0
        response = requests.get('http://otzovik.com/reviews/sberbank_rossii/order_date_desc/')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        otzivi_group = soup.find_all('div', class_='catproduct2')
        for otziv_link in otzivi_group:
            for link in otziv_link.find_all('a'):
                otziv_links.append(link['href'])
                count = count + 1
        n = 2
        while n < 4:
            URL = 'http://otzovik.com/reviews/sberbank_rossii/order_date_desc/'
            response = requests.get(URL + str(n) + '/')
            print(URL + str(n) + '/')
            soup = bs.BeautifulSoup(response.text, 'lxml')
            otzivi_group = soup.find_all('div', class_='catproduct2')
            for otziv_link in otzivi_group:
                for link in otziv_link.find_all('a'):
                    otziv_links.append(link['href'])
                    count = count + 1
            n = n + 1
        print(count)

        return otziv_links


    links = get_otziv_link()
    print(links)

    def get_otziv_info(otziv_links):
        otziv_textS= []
        for el in otziv_links:
            response = requests.get(el)
            soup = bs.BeautifulSoup(response.text, 'lxml')
            otziv_text = soup.find_all('div', {'itemprop':'description'})
            otziv_text.append(otziv_textS)
        return otziv_textS
    print(get_otziv_info(links))

    link = 'https://otzovik.com/review_5932159.html'
    response = requests.get(link)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    otziv_text = soup.find_all('div', {'itemprop':'description'})

    print(otziv_text)
