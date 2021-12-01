# coding=utf-8

import fastapi
from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import json
import time
import re
import random
from lxml import etree

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8090",
    "http://127.0.0.1:8091",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/141')
def toparticle():

    # url = 'https://www.141jav.com/date/2021/11/25'
    url = "https://www.141jav.com/date/" + \
        time.strftime('%Y/%m/%d', time.localtime())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
        # 'Cookie': '__ckguid=YrG4rXJ8PuoJGBVGCxOn4; __jsluid_s=108865343931b54fcfe7045dcb2449a9; device_id=196150170016033351554654686580fcc74e07cb0374dd08ec96e35921; smzdm_user_source=663E0FA579D5FF0C4021C60A796CCFBE; sess=YzczYmZ8MTYwNzMwODIzN3w5NzY2OTcyOTA2fDFiYmJjMmEyYmU0NzkyOGMzMjMyM2ZmYTRjNTdjMTE0; user=user%3A9766972906%7C9766972906; smzdm_id=9766972906; homepage_sug=h; r_sort_type=score; shequ_pc_sug=b; isShowGuide2=0; ss_ab=ss97; wt3_eid=%3B999768690672041%7C2160402457700357239%232160403643600470337; smzdm_user_view=9E3AE5B443F6B6B0ADA93DE951A17551; s_his=%E7%A8%BB%E5%9F%8E%2C%E9%BA%A6%E5%85%8B%E9%A3%8E%2C%E6%9C%BA%E7%AE%B1%2C%E6%98%BE%E7%A4%BA%E5%99%A8%2C%E9%BB%91%E8%8B%B9%E6%9E%9C%2C%E9%BB%91%E8%8B%B9%E6%9E%9C%E7%BD%91%E5%8D%A1; _zdmA.uid=ZDMA.O1N9s4B-n.1604543106.2419200; __jsluid_h=d98bdb55bd7bc796b6abc3c6440d0cad'
    }
    res = requests.get(url=url, headers=headers).text
    # res = json.loads(res)
    dateHtml = etree.HTML(res)
    cards = dateHtml.xpath("//div[@class = 'card mb-3']//@src")
    flagstmp = dateHtml.xpath("//div[@class = 'card mb-3']//h5/a/text()")
    magnets = dateHtml.xpath(
        "//div[@class = 'card mb-3']//a[@title='Magnet torrent']/@href")
    flags = []
    for item in flagstmp:
        item = item.split("\n")[1]
        flags.append(item)

    showlist = []
    show = {}

    for item in cards:
        i = cards.index(item)
        show["flag"] = flags[i]
        show["img"] = item
        show["magnet"] = magnets[i]
        showlist.append(show)
    time.sleep(10)

    return showlist[random.randint(0, 9)]


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
