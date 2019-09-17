import csv
import os
import re
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from fake_useragent import UserAgent
from  pyquery import  PyQuery as pq
import requests
from tqdm import tqdm
from Project import Ui_MainWindow


class Main(object):
    def __init__(self,category,numb):
        try:
            ua=UserAgent()
        except:
            ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        self.path=os.getcwd()+'\\'
        self.headers={'UserAgent':ua.random}
        self.dict_h=['书名','作者','页数','定价','出版社','出版年','ISBN','评分']
        self.url_ites=[]
        self.classify=category
        self.num=int(numb)


    def response(self,url):
        try:
            response=requests.get(url=url,headers=self.headers)
            return response
        except Exception as e :
            print("错误:",e)

    def parse_book_list(self,re,p):
        total_s='已爬取保存{num}本书籍链接'
        s='开始爬取{page}页书籍链接'
        ss=str(int((p)/20)+1)
        print(s.format(page=ss))
        htlm=re.text
        data=pq(htlm)
        URL_list=data('#subject_list > ul > li').items()
        for i,url in enumerate(URL_list):
            if i+p<self.num:
                urli=url('.pic .nbg').attr('href')
                self.url_ites.append(urli)
            else:
                print(total_s.format(num=str(self.num)))
                break

    def parce_total_url(self):
        url='https://book.douban.com/tag/{calssify}?start={page}&type=T'
        num=(int((int(self.num)/20))+1)*20
        for i in range(0,num,20):
            urli=url.format(calssify=self.classify,page=i)
            print(urli)
            response=self.response(urli)
            self.parse_book_list(response,i)
            print('书籍链接爬取完成')

    def parse_info(self):
        print("开始爬取书籍详细信息")
        items=[]
        for urli in tqdm(self.url_ites,desc='解析数据信息'):
            item={}
            print(urli)
            ret=self.response(urli)
            te=ret.text
            html=pq(te)
            info=html('#info').text()
            try:
                item['书名']=html('#wrapper h1 span').text()
                try:
                    item['作者']=re.match('作者:.*?(.*?)出',info,re.S).group(1).strip()
                except:
                    item['作者']=re.match('作者:.*?(.*?)出',info,re.S)
                try:
                    item['页数'] = re.findall('页数:(.*?)定价', info, re.S)[0].strip()
                except:
                    item['页数'] = re.findall('页数:(.*?)定价', info, re.S)
                try:
                    item['定价'] = re.findall('定价:.*?(.*?)装', info, re.S)[0].strip()
                except:
                    item['定价'] = re.findall('定价:.*?(.*?)装', info, re.S)
                try:
                    item['出版社'] = re.findall('出版社:.*?(.*?)\s出', info, re.S)[0].strip()
                except:
                    item['出版社'] = re.findall('出版社:.*?(.*?)出', info, re.S)
                try:
                    item['出版年'] = re.findall('出版年:.*?(.*?)页', info, re.S)[0].strip()
                except:
                    item['出版年'] = re.findall('出版年:.*?(.*?)页', info, re.S)
                item['ISBN']= re.findall(r'ISBN:(.*?)$',info,re.S)[0].strip()
                item['评分']= html('.rating_self.clearfix strong').text()
            except IndexError as e:
                print(e)
            items.append(item)
            time.sleep(3)
        print('爬取详细信息完成')
        return items

    def sava_data(self,data):
        print('开始写入')
        bookName='{book}书籍.csv'
        with open(self.path+bookName.format(book=self.classify),'a',encoding='utf-8-sig',newline='') as fp:
            write = csv.DictWriter(fp, fieldnames=self.dict_h)
            write.writeheader()
            for da in data:
                write.writerow(da)
        print('写入完成')

    def main(self):
        self.parce_total_url()
        print(self.url_ites)
        data=self.parse_info()
        self.sava_data(data)
        print('爬取完成')

class Runthread(QThread):
    _signal=pyqtSignal()

    def __init__(self):
        super(Runthread,self).__init__()

    def __del__(self):
        self.wait()
    def run(self) -> None:

        self._signal.emit()



class MyUiMain(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)


    def start_thread(self):
        self.thread=Runthread()
        self.thread._signal.connect(self.onClick())
        self.thread.start()

    def onClick(self):
        self.category = self.inputTxt.text()
        self.numb = self.numberInput.text()
        self.c = Main(self.category, self.numb)
        self.c.main()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MyUiMain()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())