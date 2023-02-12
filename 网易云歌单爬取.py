import requests
from bs4 import BeautifulSoup
import urllib.request
def get_redirect_url(url):
    headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    response = requests.get(url, headers=headers)
    return response.url
bo=input("1.歌曲；2.歌单，输入：")
if bo=="2":
    a=input("输入需要的内容：")
    a=a[23:-14]
    a=a.split("</a></li><li>")
    id=[]
    name=[]
    for k in range(len(a)):
        i=a[k].find("id")
        ii=a[k].find(">")
        id.append('http://music.163.com/song/media/outer/url?id='+a[k][i+3:ii-1]+'.mp3')
        name.append(a[k][ii+1:])
    print("歌单的歌名如下:{}".format(name))
    boo=input("是否正确(Y/n)")
    if boo=="Y":
        for i in range(len(name)):
            na=name[i]
            url=id[i]
            try:
                print('正在下载',na)
                urllib.request.urlretrieve(get_redirect_url(url),'D:/mp3/%s.mp3'% na)
                print('下载成功')
            except:
                print('下载失败')
    else:
        exit()
elif bo=="1":
    id=input("输入歌曲id：")
    name=input("输入歌曲名字：")
    url='http://music.163.com/song/media/outer/url?id='+id+'.mp3'
    print("正在下载{}".format(name))
    urllib.request.urlretrieve(get_redirect_url(url),'D:/mp3/%s.mp3'% name)