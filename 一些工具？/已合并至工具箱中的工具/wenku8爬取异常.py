#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#针对某个网站的小说批量爬取函数
def Pa_hjl(aid):
    url_index="https://www.wenku8.net/novel/1/{}/index.htm".format(aid)
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    rq_1=requests.get(url_index,headers=header)
    rq_1.encoding='gbk'
    html=rq_1.text
    bes=BeautifulSoup(html,"lxml")
    texts=bes.find("table", border="0")
    chapters = texts.find_all("a") 
    words = []
    for chapter in chapters:
        name = chapter.string 
        url1 = chapter.get("href")
        word = [url1, name] 
        words.append(word)
    target = words
    for tar in target:
        url='https://dl1.wenku8.com/packtxt.php?aid={}&vid={}&charset={}'.format(aid,tar[0][:5],tar[1])
        print("正在下载{}".format(tar[1]))
        driver = webdriver.Chrome()
        driver.get(url)
aid=input("请输入需要爬取的小说的aid   ")
Pa_hjl(aid)


# In[3]:





# In[22]:





# In[ ]:





# In[ ]:




