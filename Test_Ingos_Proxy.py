import requests
from requests_ntlm import HttpNtlmAuth

import requests
import json


rest_url = 'https://httpbin.org/get'
proxies = {'http': 'http://trigubov@corp.ingos.ru:Pflybwf97@mwg.corp.ingos.ru:9090',
            'https': 'https://trigubov@corp.ingos.ru:Pflybwf97@mwg.corp.ingos.ru:9090'}
test = requests.get(rest_url, proxies=proxies)
print(test.status_code)
