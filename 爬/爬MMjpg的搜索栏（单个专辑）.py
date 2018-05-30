import requests
from lxml import html
import time,os

x=0
while x<1:
    def get_image_title(url):
        response = requests.get(url).content
        selector = html.fromstring(response)
        image_title = selector.xpath("//h2/text()")[0]
        return image_title

    def get_image_amount(url):
        response = requests.get(url).content
        selector = html.fromstring(response)
        image_amount = selector.xpath("//div[@class='page']/a[last()-1]/text()")[0]
        return image_amount

    def get_image_detail_website(url):
        response = requests.get(url).content
        selector = html.fromstring(response)
        image_detail_websites = []
        image_amount = selector.xpath("//div[@class='page']/a[last()-1]/text()")[0]
        for i in range(int(image_amount)):
            image_detail_link = '{}/{}'.format(url, i+1)
            response = requests.get(image_detail_link).content
            sel = html.fromstring(response)
            image_download_link = sel.xpath("//div[@class='content']/a/img/@src")[0]
            image_detail_websites.append(image_download_link)
        return image_detail_websites

    def download_image(image_title, image_detail_websites):
        num = 1
        amount = len(image_detail_websites)
        if not os.path.exists(image_title):
            os.makedirs(image_title)

        for i in image_detail_websites:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Referer': 'http://www.mmjpg.com/search.php'

            }

            image_path = os.path.join(image_title, '%s.jpg' % num)
            print('正在下载图片：%s第%s/%s张，' % (image_title, num, amount))
            with open(image_path, 'wb') as f:
                f.write(requests.get(i,headers=header).content)
            num += 1

    if __name__ == '__main__':
        page_number = input('请输入需要爬取的专辑id：')
        i_url = 'http://www.mmjpg.com/mm/' + page_number
        time.sleep(1)
        download_image(get_image_title(i_url), get_image_detail_website(i_url))





