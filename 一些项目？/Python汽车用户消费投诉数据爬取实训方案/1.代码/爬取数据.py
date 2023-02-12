from lxml import etree
import requests as rq 
import pandas as pd
import time
cases = []
url = "http://tousu.315che.com/tousulist/serial/93/"
data_sum = rq.get(url)
data_sum.encoding = "utf-8"
dom = etree.HTML(data_sum.text,etree.HTMLParser(encoding='utf-8'))
name = dom.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/div[2]/div/a/text()')
urls = dom.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/div[2]/div/a/@href')
urls[113] = url
page_list = []
print("进入第一阶段")
for i in range(len(urls)):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    data_sum = rq.get(urls[i],headers)
    dom = etree.HTML(data_sum.text,etree.HTMLParser(encoding='utf-8'))
    if int(dom.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span/em/text()")[0]) != 0:
        max = int(dom.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/a/text()")[-1])
        print("正在爬取的品牌为:{}，该品牌网页的页数为:{}，其网址为:{}".format(name[i],max,urls[i]))
        page_list.append(max)
        print(page_list)
        for j in range(max):
            url = "{}0/0/0/{}.htm".format(urls[i],j+1)
            cases_data = rq.get(url,headers)
            dom_type = etree.HTML(cases_data.text,etree.HTMLParser(encoding="utf-8"))
            cases.append(dom_type.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li/a/@href'))
            print("正在爬第{}页".format(j+1))
    else:
        print("{}品牌无投诉".format(name[i]))
print("正在进行第二阶段")
details=[]
count_all = 0
count = 0
count_suc = 0
for i in cases:
    for j in i:
        count_all +=1
        data_case = rq.get(j,headers)
        data_case.encoding = "utf-8"
        place = [5,3,5,5,4]
        dom = etree.HTML(data_case.text,etree.HTMLParser(encoding='utf-8'))
        if not dom.xpath("/html/body/div/div[2]/div/div/p/text()"):
            detail = []
            for k in range(5):
                detail.append(dom.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[3]/p[{}]/text()".format(k+1))[0][place[k]:])
            detail.append(dom.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[1]/p/text()")[0])
            details.append(detail)
            count_suc +=1
            print("正常的个数为:{}".format(count_suc))
        else:
            count+=1
            print("不正常的个数为:{}".format(count))
#excel文件
print("正在导出为excel")
type = 0
ex = pd.DataFrame()
fac = []
kind = []
num = []
causes = []
time = []
store = []
more = []
for i in range(len(details)):
    if i == page_list[type]:
        type += 1
        print("{}excel化完成，下一个为{}".format(name[type-1],name[type]))
    fac.append(name[type])
    kind.append(details[i][0])
    num.append(details[i][1])
    causes.append(details[i][2])
    time.append(details[i][3])
    store.append(details[i][4])
    more.append(details[i][5])
ex["汽车厂商"] = fac
ex["品牌"] = kind
ex["单号"] = num
ex["投诉问题"] = causes
ex["时间"] = time
ex["进销商"] = store
ex["详细信息"] = more
ex.to_excel(r"D:/information.xlsx")
print("完成")

