# coding: utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time
import datetime
from urllib import urlopen
from bs4 import BeautifulSoup

bot = Bot(console_qr=2, cache_path="botoo.pkl")

# bot = Bot()
def zhihu():
    html=urlopen('https://daily.zhihu.com/') #打开url，获取内容
    #把html内容传到BeautifulSoup对象
    bs_obj =BeautifulSoup(html.read(), 'html.parser')
    #找到所有带有link-button的a标签
    text_list =bs_obj.find_all("a", "link-button")
    #print(text_list)

    #创建日报的list
    ribao = []
    #遍历日报内容
    for text in text_list:
        #print("***===========================***\n"+text.get_text())
        #print("https://daily.zhihu.com"+text.get("href"))
        ribao.append(text.get_text()) #添加日报标题到list中
        ribao.append("https://daily.zhihu.com"+text.get("href"))#添加日报
    html.close()
    return ribao


def tianqi_tokyo():
    html = urlopen('https://weather.yahoo.co.jp/weather/jp/13/4410.html')
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    low = bs_obj("li", "low")
    high = bs_obj("li","high")
    tanki = bs_obj("p", "pict")

    low_today=low[0]
    high_today=high[0]
    tanki_today=tanki[0]
    low_temp=low_today.get_text()
    high_temp=high_today.get_text()
    tianqi=tanki_today.get_text()

    return low_temp,high_temp,tianqi

def tianqi_gf():
    html = urlopen('https://weather.yahoo.co.jp/weather/jp/37/7200.html')
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    low = bs_obj("li", "low")
    high = bs_obj("li","high")
    tanki = bs_obj("p", "pict")

    low_today=low[0]
    high_today=high[0]
    tanki_today=tanki[0]
    low_temp=low_today.get_text()
    high_temp=high_today.get_text()
    tianqi=tanki_today.get_text()

    return low_temp,high_temp,tianqi

def tianqi_jn():
    html = urlopen('http://www.tianqi.com/junan/15/')
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    tanki = bs_obj("li", "temp")

    tanki_today=tanki[0]

    tianqi=tanki_today.get_text()

    return tianqi


def tianqi_cili():
    html = urlopen('http://www.tianqi.com/xiamen/15/')
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    tanki = bs_obj("li", "temp")

    tanki_today=tanki[0]

    tianqi=tanki_today.get_text()

    return tianqi

def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note



def send_4p():
    try:
        weather=tianqi_tokyo()
        ribao=zhihu()
        # 给自己发消息
        # bot.self.send('Hello World!')
        # 你朋友的微信名称，不是备注，也不是微信帐号。

        str = ribao[0]+ribao[1]+'\n'+ribao[2]+ribao[3]+'\n'+ribao[4]+ribao[5]+'\n'+ribao[6]+ribao[7]+'\n'+ribao[8]+ribao[9]+'\n'+ribao[10]+ribao[11]+'\n'+ribao[12]+ribao[13]+'\n'+ribao[14]+ribao[15]+'\n'+ribao[16]+ribao[17]+'\n'+ribao[18]+ribao[19]+'\n'+ribao[20]+ribao[21]+'\n'+ribao[22]+ribao[23]+'\n'+ribao[24]+ribao[25]+'\n'+ribao[26]+ribao[27]+'\n'+ribao[28]+ribao[29]
        my_friend = bot.groups().search(u'三个臭皮匠和一个诸葛恩')[0]
        my_friend.send(str)
        my_friend.send(u"今天东京的天气是"+weather[2]+",最高气温是"+weather[1]+",最低气温是"+weather[0]+",注意天气变化哦，我是气温播报机器人Bot郁")

        # 每86400秒（1天），发送1次
        t = Timer(86400, send_4p)
        t.start()
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"早间新闻发送失败了")


def send_weizhong():
    try:
        weather_jn=tianqi_jn()
        ribao=zhihu()
        str = ribao[0]+ribao[1]+'\n'+ribao[2]+ribao[3]+'\n'+ribao[4]+ribao[5]+'\n'+ribao[6]+ribao[7]+'\n'+ribao[8]+ribao[9]+'\n'+ribao[10]+ribao[11]+'\n'+ribao[12]+ribao[13]+'\n'+ribao[14]+ribao[15]+'\n'+ribao[16]+ribao[17]+'\n'+ribao[18]+ribao[19]+'\n'+ribao[20]+ribao[21]+'\n'+ribao[22]+ribao[23]+'\n'+ribao[24]+ribao[25]+'\n'+ribao[26]+ribao[27]+'\n'+ribao[28]+ribao[29]

        my_friend = bot.groups().search(u'污师大本营')[0]
        my_friend.send(str)
        my_friend.send(u"今天君安的天气是"+weather_jn+",注意天气变化哦，我是气温播报AI Robot郁")
        t=Timer(86400,send_weizhong)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"今天消息发送失败了")


def send_gf():
    try:
        contents = get_news()
        weather_gf = tianqi_gf()
        my_friend = bot.friends().search(u'地塬-')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"早安朱宝~~早饭要吃好哦")
        my_friend.send(u"今天当地的天气是"+weather_gf[2]+",最高气温是"+weather_gf[1]+",最低气温是"+weather_gf[0]+"注意天气变化哦，爱你的昆")


        t = Timer(86400, send_gf)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"下午消息发送失败了")

        

def send_family():
    try:
        weather_jn=tianqi_jn()
        ribao=zhihu()
        str = ribao[0]+ribao[1]+'\n'+ribao[2]+ribao[3]+'\n'+ribao[4]+ribao[5]+'\n'+ribao[6]+ribao[7]+'\n'+ribao[8]+ribao[9]+'\n'+ribao[10]+ribao[11]+'\n'+ribao[12]+ribao[13]+'\n'+ribao[14]+ribao[15]+'\n'+ribao[16]+ribao[17]+'\n'+ribao[18]+ribao[19]+'\n'+ribao[20]+ribao[21]+'\n'+ribao[22]+ribao[23]+'\n'+ribao[24]+ribao[25]+'\n'+ribao[26]+ribao[27]+'\n'+ribao[28]+ribao[29]

        my_friend = bot.groups().search(u'郁氏集团')[0]
        my_friend.send(str)
        my_friend.send(u"今天莒南的天气是"+weather_jn+",注意天气变化哦，我是气温播报AI Robot郁")
        t=Timer(86400,send_weizhong)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"今天消息发送失败了")


def send_ayi():
    try:
        ribao=zhihu()
        str = ribao[0]+ribao[1]+'\n'+ribao[2]+ribao[3]+'\n'+ribao[4]+ribao[5]+'\n'+ribao[6]+ribao[7]+'\n'+ribao[8]+ribao[9]+'\n'+ribao[10]+ribao[11]+'\n'+ribao[12]+ribao[13]+'\n'+ribao[14]+ribao[15]+'\n'+ribao[16]+ribao[17]+'\n'+ribao[18]+ribao[19]+'\n'+ribao[20]+ribao[21]+'\n'+ribao[22]+ribao[23]+'\n'+ribao[24]+ribao[25]+'\n'+ribao[26]+ribao[27]+'\n'+ribao[28]+ribao[29]
        weather_cili = tianqi_cili()
        my_friend = bot.friends().search(u'雨后的早晨')[0]
        my_friend.send(str)
        my_friend.send(u"阿姨早上好!今天厦门的天气是" + weather_cili + ",注意天气变化哦")


        t = Timer(86400, send_gf)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"下午消息发送失败了")




def morning():
    h = 07
    m = 00

    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(20)
    chat()




def chat():
    if __name__ == "__main__":
        send_4p()
        send_gf()
        send_weizhong()
        send_family()
        send_ayi()



morning()


#send_4p()
