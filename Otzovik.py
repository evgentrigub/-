import requests
import bs4 as bs
import time
from openpyxl import Workbook


class Otzovik:
    def get_feedback_link():
        feedback_links = []
        count = 0
        response = requests.get('http://otzovik.com/reviews/sberbank_rossii/order_date_desc/')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        feedback_group = soup.find_all('div', class_='catproduct2')
        for feedback_link in feedback_group:
            for link in feedback_link.find_all('a'):
                feedback_links.append(link['href'])
                count = count + 1
                time.sleep(5)
        n = 2
        while n < 4:
            URL = 'http://otzovik.com/reviews/sberbank_rossii/order_date_desc/'
            response = requests.get(URL + str(n) + '/')
            print(URL + str(n) + '/')
            soup = bs.BeautifulSoup(response.text, 'lxml')
            feedback_group = soup.find_all('div', class_='catproduct2')
            for feedback_link in feedback_group:
                for link in feedback_link.find_all('a'):
                    feedback_links.append(link['href'])
                    count = count + 1
                    time.sleep(5)
            n = n + 1
        print(count)

        return feedback_links

    def get_feedback_info(feedback_links):
        feedback_textS = []
        for el in feedback_links:
            response = requests.get(el)
            soup = bs.BeautifulSoup(response.text, 'lxml')
            feedback_text = soup.find_all('div', {'itemprop': 'description'})
            feedback_text.append(feedback_textS)
            time.sleep(5)
        return feedback_textS

    links = get_feedback_link()
    print(links)
    print(get_feedback_info(links))

    link = 'https://otzovik.com/review_5932159.html'
    response = requests.get(link)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    feedback_text = soup.find_all('div', {'itemprop': 'description'})

    print(feedback_text)
