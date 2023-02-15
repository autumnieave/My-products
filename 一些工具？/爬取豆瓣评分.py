import PySimpleGUI as sg 
from lxml import etree
import requests as rq
import pandas as pd

 
def pa_douban(id,namee):
    url = "https://movie.douban.com/subject/{}/comments?start=0&limit=120&status=P&sort=new_score".format(id)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    data = rq.get(url,headers = header)
    comment = []
    support = []
    time = []
    name = []
    count = 0
    while str(data) != "<Response [404]>":
        count += 1
        count_not = 0
        dom = etree.HTML(data.text, etree.HTMLParser(encoding='utf-8')) 
        if len(dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div/p/span/text()")) == 0:
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[3]/div/div/p/span/text()"):
                comment.append(i)
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[3]/div/div/h3/span[2]/a/text()"):
                name.append(i)
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[3]/div/div/h3/span[2]/span[3]/@title"):
                time.append(i)
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[3]/div/div/h3/span[2]/span[2]/@title"):
                if i.find(":") != -1:
                    support.append("该用户未评分")
                    time.insert(count_not+120*count_not-1,i)
                    count_not += 1 
                else:
                    support.append(i)    
        else: 
            for i in (dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div/p/span/text()")):
                comment.append(i)   
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div/h3/span[2]/a/text()"):
                name.append(i)
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div/h3/span[2]/span[3]/@title"):
                time.append(i)
            for i in dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div/h3/span[2]/span[2]/@title"):
                if i.find(":") != -1:
                    support.append("该用户未评分")
                    time.insert(count_not+120*count_not-1,i)
                    count_not += 1
                else:
                    support.append(i)
                    count_not += 1
        url = "https://movie.douban.com/subject/{}/comments?start={}&limit=120&status=P&sort=new_score".format(id,120*count)
        data = rq.get(url,headers = header)
    file = pd.DataFrame()
    file["用户名"] = name
    file["态度"] = support
    file["评论时间"] = time
    file["具体评论"] = comment
    file.to_excel("D:/{}.xlsx".format(namee),index=False)
    sg.Print("完成")

sg.theme('SandyBeach')

layout=[
        [sg.Text("输入电影的id："),sg.Input(key="id",size=(15,1),text_color='blue')],
        [sg.Text("输入电影名："),sg.Input(key="name",size=(15,1),text_color='blue'),sg.Button("执行"),sg.Button("关闭程序")]
       ]

window=sg.Window("豆瓣评分爬取",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("执行"):
        pa_douban(values["id"],values["name"])
window.close()