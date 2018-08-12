import requests
from lxml import html


HEADERS = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
           }

LOGIN_URL = 'https://github.com/login'
SESSION_URL = 'https://github.com/session'


s = requests.session()

resp = s.get(LOGIN_URL, headers=HEADERS)

tree = html.fromstring(resp.text)

token = tree.xpath('//input[@name="authenticity_token"]/@value')[0]

data = {
"commit": "Sign in",
"utf8": "✓",
"authenticity_token": token,
"login": "biscuit36@163.com",
"password": "",
}

resp_login = s.post(SESSION_URL, data=data, headers=HEADERS).text

print(resp_login)
