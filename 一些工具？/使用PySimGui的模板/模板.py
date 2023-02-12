import PySimpleGUI as sg 

 
def m():
    sg.Print("我是模板")

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
    if event in ("执行"):
        m()
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()
