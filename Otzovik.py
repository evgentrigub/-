import requests
import bs4 as bs
import time
from openpyxl import Workbook


class Otzovik:

    def get_feedback_link():
        feedback_links = []
        URL = 'https://otzovik.com/reviews/strahovaya_kompaniya_ingosstrah_russia_moscow/order_date_desc/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"}
        # proxy_list = Proxy.get_proxy_list()
        # proxy = Proxy.get_proxy(proxy_list)
        # proxy2 = proxy
        proxies = {
            'http':'http://128.199.129.5:80	'
        }
        response = requests.get(URL, headers=headers, proxies=proxies)
        soup = bs.BeautifulSoup(response.text, 'lxml')
        feedback_group = soup.find_all('div', class_='review-bar')
        i = 0
        for group in feedback_group:
            for el in group.find_all('a'):
                if (i%2==0):
                    a = el['href']
                    feedback_links.append(a)
                i += 1

        # n = 2
        # while n < 4:
        #     response = requests.get(URL + str(n) + '/', headers=headers, proxies = proxy2)
        #     print(URL + str(n) + '/')
        #     soup = bs.BeautifulSoup(response.text, 'lxml')
        #     feedback_group = soup.find_all('div', class_='catproduct2')
        #     for feedback_link in feedback_group:
        #         for link in feedback_link.find_all('a'):
        #             feedback_links.append(link['href'])
        #             count = count + 1
        #     n = n + 1
        # print(count)

        return feedback_links

    def get_feedback_info(feedback_links):
        feedback_textS = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36(KHTML, like Gecko) Chrome",
            "Accept": "text/html,application/xhtml+xml,application/xml; q = 0.9, image / webp, * / *;q = 0.8"}
        proxies = {
            'http': 'http://128.199.129.5:80	'
        }
        for el in feedback_links:
            response = requests.get(el, headers=headers, proxies=proxies)
            if response.status_code == 200:
                soup = bs.BeautifulSoup(response.text, 'lxml')
                feedback_text = soup.find('div', {'itemprop': 'description'})
                feedback_textS.append(feedback_text)
            else:
                print("Fuck!")
        return feedback_textS

    links = get_feedback_link()
    print(links)
    # print(get_feedback_info(links))

    # link = 'https://otzovik.com/review_5932159.html'
    # response = requests.get(link)
    # soup = bs.BeautifulSoup(response.text, 'lxml')
    # feedback_text = soup.find('div', {'itemprop': 'description'})
    # print(feedback_text)
