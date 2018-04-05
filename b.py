#サイトの画像URL取得
import urllib.request
import bs4
import os
import time
#url = "https://search.yahoo.co.jp/image/search?ei=UTF-8&fr=sfp_as&aq=-1&oq=&ts=2406&p=%E3%83%94%E3%82%AB%E3%83%81%E3%83%A5%E3%82%A6&meta=vc="
#url="https://search.yahoo.co.jp/image/search?p=ピカチュウ&search.x=1&tid=top_ga1_sa&ei=UTF-8&aq=-1&oq=ピカチュウ&ai=ZxjGa2pET3CuwckLL5TU.A&ts=1955&fr=top_ga1_sa"
#url="https://search.yahoo.co.jp/image/search;_ylt=A2RioudeIsJa_VsATiaU3uV7?p=yahoo&aq=-1&oq=&ei=UTF-8"
import sys
argvs=sys.argv
url=argvs[1]
#url="https://search.yahoo.co.jp/image/search?ei=UTF-8&fr=sfp_as&aq=-1&oq=&ts=5293&p=%E9%95%B7%E6%BF%B1%E3%81%AD%E3%82%8B&meta=vc="
#print(urlt)
#print(ult)
request = urllib.request.urlopen(url)
html = request.read()

#print(html)
encoding_list=["utf-8","utf_8","euc_jp","euc_jis_2004", "euc_jisx0213", "shift_jis","shift_jis_2004","shift_jisx0213", "iso2022jp","iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_3","iso2022_jp_ext","latin_1", "ascii"]
#html.decode("shift_jis")
#print(html.decode("shift_jis"))
for enc in encoding_list:
    try:
#もしかしたらutf8にする必要があるかも
        html.decode(enc)
        break
    except:
        enc = None

resources = []
soup = bs4.BeautifulSoup(html)
extensions=[".jpg",".jpeg",".png",".gif"]
for a_tag in soup.find_all("a"):
    href_str = a_tag.get("href")
    #if href_str.startswith("h"):
    try:
        (path, ext) = os.path.splitext(href_str)
        if ext in extensions:
            resources.append(href_str)
    except:
        pass
resources=sorted(set(resources),key=resources.index)

for resource in resources:
#    print(resource)
    try:
        request=urllib.request.urlopen(resource)
        f=open(os.path.basename(resource),"wb")
        f.write(request.read())
    except Exception as e:
        print(e)
    finally:
        time.sleep(3)
