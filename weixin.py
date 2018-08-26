#coding:utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot(console_qr=2,cache_path="botoo.pkl")

# bot = Bot(console_qr=2,cache_path="botoo.pkl")


def get_news():


    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():

        contents = get_news()

        bot.self.send('ceshi汉字')
        #my_friend = bot.friends().search(u'Wyane')[0]
        t = Timer(10, send_news)
        t.start()


if __name__ == "__main__":
    send_news()