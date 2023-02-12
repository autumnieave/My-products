import requests
from bs4 import BeautifulSoup
#针对某个网站的小说批量爬取函数
def Pa_hjl(url_index,url):
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    rq_1=requests.get(url_index,headers=header)
    rq_1.encoding='gbk'
    html=rq_1.text
    bes=BeautifulSoup(html,"lxml")
    texts=bes.find("table", border="0")
    chapters = texts.find_all("a") 
    words = []
    for chapter in chapters:
        name = chapter.string 
        url1 = url + chapter.get("href")
        word = [url1, name] 
        words.append(word)
    target = words
    i=1
    for tar in target:
        req = requests.get(url=tar[0],headers = header)
        req.encoding = 'gbk'
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("div", id = "content")
        texts_list = texts.text.split("\xa0"*4)
        with open("D:/{}.txt".format(i),"w",encoding='utf-8') as file: 
            file.write(tar[1]+"\n")
            for line in texts_list:
                file.write(line+"\n")
        i=i+1
url_index=input("请输入需要爬取的小说的目录网页")
url=input("请输入上面输入的网址但去除后面的\index")
Pa_hjl(url_index,url)




