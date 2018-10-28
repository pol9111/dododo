import requests
from mail import send_mail
from config import *
import json


def login_in():
    try:
        resp = requests.post(URL, headers=HEADERS, data=FORMDATA)
        rst = json.loads(resp.text)
        info = rst.get('info')

        if info == '登录成功！':
            CONTENT = '人人影视登录成功!'
            send_mail(MY_SENDER, MY_PASS, MY_USER, content=CONTENT)
            print(CONTENT)

        else:
            CONTENT = '人人影视登入失败!'
            send_mail(MY_SENDER, MY_PASS, MY_USER, content=CONTENT)
            print(CONTENT)

    except Exception as e:
        CONTENT = '人人影视登入失败!'
        send_mail(MY_SENDER, MY_PASS, MY_USER, content=CONTENT)
        print(CONTENT)
        print(e)

login_in()