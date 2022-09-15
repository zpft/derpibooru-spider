import requests
from lxml import etree
import time


UserAgent = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}  


#爬的页数 就是没登陆的情况下可以看到的图片 看不到的会自动跳过
for x in range(7,14,1):
    requests.DEFAULT_RETRIES = 10
    url = "https://derpibooru.org/search?page=@&sd=desc&sf=upvotes&q=score.gte%3A1000%2C-equestria+girls%2C-suggestive"
    url = url.replace("@", str(x))
    resp = requests.get(url)
    html = etree.HTML(resp.text)

    divs = html.xpath("/html/body/div/main/div/div[1]/div")
    try:
        for div in divs:              
            imgurl = div.xpath("./div[2]/div/a/picture/img/@src")

            for i in imgurl:
                imgurl = i

            print(str(imgurl) + "图片url已抓取！")

            imgname = div.xpath("./div[2]/div/a/picture/img/@alt")

            for j in imgname:
                imgname = j

            #重命名呆站文件名，使其成为合法路径

            imgname = imgname.replace(":", "：")
            imgname = imgname.replace("*", " ")
            imgname = imgname.replace("/", " ")
            imgname = imgname.replace("|", " ")

            namef = imgname[0:100]
            nameb = imgurl[-6:]

            imgname = namef + nameb
            print(imgname+ "图片name已修正！")

            respfinal = requests.get(imgurl,headers = UserAgent)

            with open("D:\\img\\{}".format(imgname), "wb") as f:
                    f.write(respfinal.content)

            print("编号为 "  + str(imgurl) + "的图片已成功下载至img文件夹！")


            time.sleep(1)
            s = requests.session()
            s.keep_alive = False
            resp.close()
    except:
        print("\n" +"坏了,编号为#" + str(imgurl) + "的图片搞不定" + "\n")

print("\n" + "————————————————————————————————————ALL process is OVER!————————————————————————————————————" + "\n")


