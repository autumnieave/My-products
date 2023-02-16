import PySimpleGUI as sg 
import pandas as pd
 
def m():
    sg.Print("我是模板")

def count(path,name):
    data = pd.read_excel(path)
    sg.Print(data[name].value_counts())

def clear(name,path):
    data=pd.read_excel(path)
    sg.Print(path)
    count=0
    boo=1
    for i in data[name]:
        length=len(i)
        if(i[length-1]==" "):
            data[name][count]=i[:length-1]
            sg.Print("名字后有空格的为：{}".format(i))
            boo=0
        count=count+1
    data.to_excel(path,index = False)
    if(boo==1):
        sg.Print("数据正常，无需修改")
    else:
        sg.Print("已完成，修改后的文件为{}".format(path))
    
def delete_same(name,path):
    sg.Print("reading file")
    data = pd.read_excel(path)
    sg.Print("start")
    data = data.drop_duplicates(subset=[name],keep='first')
    sg.Print("outing")
    filename = path
    while filename.find("/") != -1:
        filename = filename[filename.find("/")+1:]
    file_dir = path[:len(path)-len(filename)-1]
    data.to_excel("{}/pure.xlsx".format(file_dir))
    sg.Print("finish")
sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text("输入列的头名称："),sg.Input(key="name",size=(15,1),text_color='blue')],
        [sg.FileBrowse('选择文件',key='file',target="filename"),sg.Button("去重"),sg.Button("查看列数据"),sg.Button("查看空格？"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("Excel处理",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("查看列数据"):
        path = values["file"]
        name = values["name"]
        count(path,name)
    if event in ("查看空格？"):
        path = values["file"]
        name = values["name"]    
        clear(name,path)
    if event in ("去重"):
        path = values["file"]
        name = values["name"]
        delete_same(name,path)
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是备注")
window.close()
