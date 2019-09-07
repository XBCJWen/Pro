import csv
import os
import re
import time
from fake_useragent import UserAgent
from  pyquery import  PyQuery as pq
import requests
from tqdm import tqdm


class Main(object):
    def __init__(self):
        ua=UserAgent()
        self.path=os.getcwd()+'\\'
        self.headers={'UserAgent':ua.random}
        self.dict_h=['书名','作者','页数','定价','出版社','出版年','ISBN','评分']
        self.url_ites=[]
        self.output_info()
        self.classify=input("请输入分类:")
        self.num=int(input("请输入爬取数:"))


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

    def output_info(self):
        print('''文学 · · · · · ·
小说(5954853)	外国文学(2260203)	文学(2012837)	随笔(1273858)
中国文学(1271577)	经典(1264828)	日本文学(989651)	散文(766379)
村上春树(475552)	诗歌(374004)	童话(336694)	儿童文学(290461)
名著(289569)	古典文学(278123)	王小波(252523)	余华(250469)
杂文(236254)	张爱玲(206440)	当代文学(194563)	外国名著(128519)
钱钟书(124692)	鲁迅(108613)	诗词(93890)	茨威格(71577)
米兰·昆德拉(58673)	杜拉斯(46107)	港台(8708)
流行 · · · · · ·
漫画(1384534)	推理(1082943)	绘本(989003)	青春(726258)
东野圭吾(686623)	科幻(625654)	悬疑(624559)	言情(555093)
奇幻(370119)	武侠(345324)	推理小说(342683)	日本漫画(321082)
耽美(284006)	韩寒(267829)	网络小说(241143)	亦舒(240312)
三毛(232095)	科幻小说(208047)	阿加莎·克里斯蒂(182915)	安妮宝贝(176110)
金庸(172382)	穿越(161846)	郭敬明(156436)	轻小说(150290)
魔幻(139432)	青春文学(134597)	几米(119032)	J.K.罗琳(102921)
幾米(102625)	张小娴(98278)	古龙(79839)	高木直子(75738)
校园(70724)	沧月(67336)	余秋雨(59045)	落落(58541)
文化 · · · · · ·
历史(2433161)	心理学(1582476)	哲学(1352939)	传记(876224)
社会学(873696)	文化(830803)	艺术(597804)	社会(515872)
设计(443996)	政治(435284)	建筑(294870)	宗教(293480)
电影(277278)	政治学(272408)	数学(257041)	中国历史(223432)
回忆录(204118)	思想(184608)	国学(166671)	人物传记(151514)
艺术史(143905)	人文(142435)	音乐(135659)	绘画(128963)
戏剧(122644)	西方哲学(97073)	二战(89072)	近代史(88097)
军事(84524)	佛教(83116)	考古(59803)	自由主义(50974)
美术(45466)
生活 · · · · · ·
爱情(1079523)	成长(707586)	生活(633091)	旅行(603415)
心理(500253)	励志(447949)	女性(414751)	摄影(323295)
教育(262923)	职场(234621)	美食(214769)	游记(168569)
灵修(134194)	健康(98126)	情感(96696)	人际关系(55183)
两性(52967)	手工(42498)	养生(40282)	家居(27433)
自助游(2740)
经管 · · · · · ·
经济学(493283)	管理(475904)	经济(403011)	商业(366519)
金融(320082)	投资(267993)	营销(176825)	理财(135587)
创业(128081)	股票(74422)	广告(73484)	企业史(25425)
策划(9547)
科技 · · · · · ·
科普(704504)	互联网(267070)	编程(176327)	科学(163917)
交互设计(73883)	用户体验(60129)	算法(59048)	科技(33396)
web(22431)	交互(5579)	通信(5420)	UE(5375)
UCD(3598)	神经网络(3429)	程序(1335)''')


if __name__ == '__main__':
    c=Main()
    c.main()