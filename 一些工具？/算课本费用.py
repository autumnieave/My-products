import PySimpleGUI as sg 
import pandas as pd
 
def price(path1,path2,classs,name):
    df = pd.read_excel(path1,sheet_name=classs)
    df_price = pd.read_excel(path2)
    df = df.loc[df["姓名"] == name]
    ls = []
    for i in df["教材名称"]:
        if i != "":
            count = 0 
            for j in df_price["书名"]:
                if i[:3] == j[:3]:
                    sg.Print(i)
                    sg.Print(df_price["单价"][count])
                    ls.append(df_price["单价"][count])
                count += 1
    sg.Print("价格为{}".format(sum(ls)))

sg.theme('SandyBeach')

layout=[
        [sg.Text('文件1：',font=("微软雅黑", 12)),sg.Text('',key='filename1',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text('文件2：',font=("微软雅黑", 12)),sg.Text('',key='filename2',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text("名字："),sg.Input(key="name",size=(15,1),text_color='blue')],
        [sg.Text("班级："),sg.Input(key="class",size=(15,1),text_color='blue')],
        [sg.FileBrowse('选择文件1',key='file1',target="filename1"),sg.FileBrowse('选择文件2',key='file2',target="filename2"),sg.Button("执行"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("Excel处理",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("执行"):
        price(values["file1"],values["file2"],values["class"],values["name"])
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()