# coding: utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time
import datetime

bot = Bot(console_qr=1, cache_path="botoo.pkl")

# bot = Bot()


def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news1():
    try:
        contents = get_news()
        # 给自己发消息
        # bot.self.send('Hello World!')
        # 你朋友的微信名称，不是备注，也不是微信帐号。

        my_friend = bot.friends().search(u'地塬-')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"早安~~早饭要吃哦")
        # 每86400秒（1天），发送1次
        t = Timer(86400, send_news1)
        t.start()
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"早间新闻发送失败了")


def send2():
    try:
        my_friend = bot.friends().search(u'地塬-')[0]
        my_friend.send(u"中午记得吃饭，注意防晒")
        t=Timer(86400,send2)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"今天消息发送失败了")


def send3():
    try:
        my_friend = bot.friends().search(u'地塬-')[0]
        my_friend.send(u"吃饭了么记得早点吃晚饭")
        t = Timer(86400, send2)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"下午消息发送失败了")


def send4():
    try:
        my_friend = bot.friends().search(u'地塬-')[0]
        my_friend.send(u"我睡觉了晚安，好梦，么么哒")
        t = Timer(86400, send2)
        t.start()
    except:
        my_friend = bot.friends().search('肉松君')[0]
        my_friend.send(u"晚间消息失败了")


def morning():
    h = 07
    m = 10

    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(20)
    chat()


def noon():
    h = 12
    m = 22

    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(20)
    chat2()


def evening():
    h = 18
    m = 45

    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(20)
    chat3()


def night():
    h = 00
    m = 59

    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(20)
    chat4()


#time.strftime("%H:%M:%S")
#cur=datetime.datetime.now()


def chat():
    if __name__ == "__main__":
        send_news1()


def chat2():
    if __name__ == "__main__":
        send2()


def chat3():
    if __name__ == "__main__":
        send3()


def chat4():
    if __name__ == "__main__":
        send4()


morning()

noon()

evening()

night()

