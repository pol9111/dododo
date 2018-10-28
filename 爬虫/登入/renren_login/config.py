# URL = 'http://www.zimuzu.io/user/login'

# URL = 'http://www.zimuzu.io/User/Login/ajaxLogin'
URL = 'http://www.zimuzu.tv/User/Login/ajaxLogin'


HEADERS = {
    'Connection': 'keep-alive',
    'Content-Length': '127',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://www.zimuzu.io',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.zimuzu.io/user/login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
           }

FORMDATA = {
    'account': 'biscuit36@163.com',
    'password': 'r71r711380MRTW',
    'remember': 1,
    'url_back': 'http://www.zimuzu.tv/',
    # 'url_back': 'http://www.zimuzu.io/',

}

MY_SENDER = 'biscuit36@163.com'  # 发件人邮箱账号
MY_PASS = 'fd83ra'  # 发件人邮箱密码
MY_USER = 'biscuit36@163.com'  # 收件人邮箱账号，我这边发送给自己