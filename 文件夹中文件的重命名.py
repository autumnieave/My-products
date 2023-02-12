import PySimpleGUI as sg 
import os
 
def rename(path):
    files=os.listdir(path)
    type=files[0][files[0].find(".")+1:]
    sg.Print("格式为{}".format(type))
    count=1
    files=os.listdir(path)
    for i in files:
        sg.Print("重命名{}为{}.{}".format(i,count,type))
        os.rename("{}/{}".format(path,i),"{}/{}.{}".format(path,count,type))
        count=count+1

sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件夹为:',font=("微软雅黑", 12)),sg.Text('',key='fold',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.FolderBrowse("选择文件夹",target='fold',key='folder'),sg.Button("执行"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("重命名",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("执行"):
        rename(values["folder"])
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()