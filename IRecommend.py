import requests
import bs4 as bs
import time
from openpyxl import Workbook

class IRecommend:
    def get_feedback_link():
        URL = 'http://irecommend.ru'
        feedback_links = []
        count = 0
        response = requests.get('http://irecommend.ru/content/sberbank?new=1')
        soup = bs.BeautifulSoup(response.text, 'lxml')
        feedback_group = soup.find_all('div', class_='nobr')
        for feedback_link in feedback_group:
            for link in feedback_link.find_all('a'):
                feedback_links.append(URL + link['href'])
                count = count + 1
        print(count)

        return feedback_links


    links = get_feedback_link()
    #print(links)


