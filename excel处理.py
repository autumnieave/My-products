import pandas as pd    
import PySimpleGUI as sg 
import re
 
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
    data.to_excel(path)
    if(boo==1):
        sg.Print("数据正常，无需修改")
    else:
        sg.Print("已完成，修改后的文件为{}".format(path))

sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.Text("输入列的头名称："),sg.Input(key="name",size=(15,1),text_color='blue')],
        [sg.FileBrowse('选择文件',key='file',target="filename"),sg.Button("执行"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("Excel处理",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='xlsx':
        sg.Print("成功识别excel文档")
        fileName=values['file']
        clear(values["name"],fileName)
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("此程序只可进行字符的文件操作，数字的不行，如有需要可自行调整代码，且仅支持xlsx格式，均微调后即可实现")
window.close()