import requests
import re
from lxml import etree
import time



x = 1
start = 2946798
end = 1
for x in range(start,end,-1):
    requests.DEFAULT_RETRIES = 10

    time.sleep(0.1)

    s = requests.session()
    s.keep_alive = False

    number = x

    UserAgent = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
    }   

    url = "https://derpibooru.org/images/x"
    url = url.replace("x", str(number))
    # try:
    resp = requests.get(url,headers = UserAgent)

    html = etree. HTML(resp.text)

    imgurl = html.xpath("/html/head/meta[last()]/@content")

    print(imgurl)

    for i in imgurl:
        imgurlstr = i

    print("已抓取图片编号为 "  + str(number) + " 的url:")
    print(imgurlstr)

    imgname = html.xpath("/html/head/title/text()")

    for j in imgname:
        imgnamestr = j

    imgnamestr = imgnamestr.replace(":", "：")
    imgnamestr = imgnamestr.replace("*", " ")
    imgnamestr = imgnamestr.replace("/", " ")

    namef = imgnamestr[0:100]
    nameb = imgurlstr[-6:]
    print(nameb)
    imgnamestr = namef + nameb

    print("图片编号为 "  + str(number) + " 的name已经被修正为:")
    print(imgnamestr)

    respfinal = requests.get(imgurlstr,headers = UserAgent)

    with open("D:\\img\\{}".format(imgnamestr), "wb") as f:
            f.write(respfinal.content)

    print("编号为 "  + str(number) + "的图片已成功下载至img文件夹！")

    s = requests.session()
    s.keep_alive = False
    resp.close()
    # except:
    #     print("\n" +"坏了,编号为#" + str(number) + "的图片搞不定，应该是被删除了" + "\n")

print("\n" + "————————————————————————————————————ALL process is OVER!————————————————————————————————————" + "\n")


