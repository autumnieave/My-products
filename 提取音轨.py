from moviepy.editor import *
import PySimpleGUI as sg 
import re

def mp4Tomp3(mp4Path):
    video = VideoFileClip(mp4Path)
    list_filepath = list(mp4Path)
    if list_filepath[-1] == '4':
        list_filepath[-1] = '3'
        mp3Path = ''.join(list_filepath)
        # MP3文件的路径
        sg.Print(mp3Path)
        audio = video.audio
        audio.write_audiofile(mp3Path)

sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.FileBrowse('选择文件',key='file',target="filename"),sg.Button("执行"),sg.Button("关闭程序"),sg.Button("备注")]
       ]

window=sg.Window("Excel处理",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='mp4':
        sg.Print("成功识别mp4文件")
        fileName=values["file"]
        mp4Tomp3(fileName)
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()


