import requests
import re
import time
import json
import os

#path：需要清理的文件名
#清洗掉windows系统非法文件夹名字
def strip(path):
    path = re.sub(r'[?\\*|“<>:/]','',str(path))
    return path

#爬虫类
class Spider:
    #模仿浏览发送请求
    def __init__(self):
        self.session = requests.Session()
    #核心部分，run，4，5,6部分
    def run(self,start_url):
        img_ids=self.get_img_item_ids(start_url)
        for img_id in img_ids:
            img_item_info=self.get_img_item_info(img_id)
            self.save_img(img_item_info)

    #下载器被4,5,6,部分利用
    def download(self,url):
        try:                  #成功return，错误打印异常
            return self.session.get(url)
        except Exception as e:
            print(e)

    #返回套图id列表（获取主页所有套图的url）
    def get_img_item_ids(self,start_url):
        response=self.download(start_url)
        if response:
            html=response.text
            ids= re.findall(r'http://tu.duowan.com/gallery/(\d+).html',html)
            return set(ids)          #集合不重复id

        #根据套图ID获取套图的信息（方便第6部分创建文件夹）
    def get_img_item_info(self,img_id):
        img_item_url="http://tu.duowan.com/index.php?r=show/getByGallery/&gid=%s&_=%s" %(img_id,int(time.time()*1000))
        response=self.download(img_item_url)
        if response:
            return json.loads(response.text)

    #根据套图信息，持久化（根据套图信息创建文件夹命名，后缀并保存）
    def save_img(self,img_item_info):
        dir_name=strip(img_item_info['gallery_title'])
        print(dir_name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for img_info in img_item_info['picInfo']:
            img_name=strip(img_info['title'])
            img_url=img_info['url']
            pix=(img_url.split('/')[-1]).split('.')[-1]       #图片后缀
            img_path=os.path.join(dir_name,"%s.%s"%(img_name,pix))   #图片全路径
            if not os.path.exists(img_path):
                response=self.download(img_url)
                print(img_url)
                if response:
                    img_data=response.content
                    with open(img_path,'wb') as f:
                        f.write(img_data)

#如果是本模块则调用，以下部分私有化，不被其他模块调用
if __name__ == '__main__':
    spider=Spider()
    start_url = 'http://tu.duowan.com/m/meinv'
    spider.run(start_url)









