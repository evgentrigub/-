import bs4
import requests

def get_proxy_list():
    proxy_url = "https://www.ip-adress.com/proxy-list"
    proxy_list = []
    response = requests.get(proxy_url)
    # str = html.fromstring(r.content)
    # result = str.xpath("//tr[@class='odd']/td[1]/text()")
    # self.proxy_list = result
    soup = bs4.BeautifulSoup(response.text, "lxml")
    proxy_group = soup.find('table', class_="htable proxylist")
    i = 0
    for el in proxy_group.find_all('td'):
        if (i % 4 == 0):
            server_port = el.text
            proxy_list.append(server_port)
        i += 1
    print(proxy_list)
    return proxy_list

def get_proxy(proxy_list):
    for proxy in proxy_list:
        url_try_to_get = url = "http://otzovik.com/"
        url = "http://" + proxy
        print(url)
        proxies = {
            'http': url,
        }
        try:
            r = requests.get(url_try_to_get, proxies=proxies)
            if r.status_code == 200:
                print("Success! This proxy is good: " + url)
                return url
        except requests.exceptions.ConnectionError:
            continue

proxy_list = get_proxy_list()
proxy_list_el = get_proxy(proxy_list)