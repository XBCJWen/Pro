# # #
# # # class main:
# # #     def __init__(self,fun):
# # #         self.fun=fun
# # #
# # #     def __call__(self, *args, **kwargs):
# # #         print("添加的功能")
# # #         c = self.fun(*args, **kwargs)
# # #         return c
# # #
# # #
# # # @main
# # # def sum(a,b):
# # #     print("值为",a+b)
# # #
# # # if __name__ == '__main__':
# # #     sum(10,5)
# # # import threading
# # #
# # #
# # # def ss():
# # #     print("thread %s runing..." % threading.current_thread().name)
# # #
# # # def sss():
# # #     print("thread %s runing..." % threading.current_thread().name)
# # #
# # # print("thread %s runing..."%threading.current_thread().name)
# # #
# # #
# # #
# # # c=threading.Thread(target=ss,name="threadOne")
# # # t=threading.Thread(target=sss,name="threadTwo")
# # #
# # #
# # # c.start()
# # # t.start()
# # #
# # # c.join()
# # # t.join()
# # #
# # import  threading
# # class t(threading.Thread):
# #     money=100
# #     def __init__(self,name):
# #         threading.Thread.__init__(self)
# #         self.nmae = name
# #         self.lock=threading.Lock()
# #
# #
# #     def run(self):
# #         global  money
# #         money=100
# #         print(money)
# #         self.lock.acquire()
# #         for i in range(50):
# #
# #             print("threadName {name} runing...".format(name=self.name),money)
# #             money=money-1
# #         self.lock.release()
# #
# #
# #
# # print(threading.current_thread().name)
# # c=t("onw")
# # a=t("two")
# #
# #
# # c.start()
# # a.start()
# #
# # c.join()
# # a.join()
# # import os
# # from multiprocessing import Process, Lock, Pool
# #
# #
# # def t():
# #     for i in range(1000000):
# #         print(i)
# #     print("thradName   {name} thrading...".format(name=os.getpid()))
# #
# # if __name__ == '__main__':
# #     print("thradName   {name} thrading...".format(name=os.getpid()))
# #     p=Pool(2)
# #     p.apply_async(t())
#
#
# # def consumer(name):
# #     print("自主运行",name)
# #     b=yield
# #     print("接收的b{}".format(b))
# #
# #
# #
# # def producer(o):
# #     o.send(None)  # 必须先发送None
# #     print("小弟运行")
# #     o.send(2)
# #
# #
# # if __name__ == '__main__':
# #     con1 = consumer('消费者A')  # 创建消费者对象
# #     producer(con1)
#
# # import  greenlet
# #
# # def A():
# #     print("1")
# #     g2.switch()
# #     print("3")
# #     g2.switch()
# # def B():
# #     print(2)
# #     g1.switch()
# #     print("4")
# #
# # g1=greenlet.greenlet(A)
# # g2=greenlet.greenlet(B)
# # g1.switch()
# import os
# import re
# import time
# #
# # #
# # import requests
# #
# # response = requests.get(url=, headers=self.headers)
# # print(response.text)
# s='sdaf夺基本面塔顶枯塔顶1313阿斯蒂芬模压 基本面' \
#   '顶戴无可奈何无可奈何花落去枯萎'
# s=re.match('s(.*?)9',s,re.S).group()
# print(s)
import  pip
print(pip.pep425tags.get_supported())