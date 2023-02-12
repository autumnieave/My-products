from moviepy.editor import *
import os
from natsort import natsorted
import PySimpleGUI as sg 


def combine_mp4(path):
    # 定义一个数组
    L = []

    # 访问 video 文件夹 (假设视频都放在这里面)
    for root, dirs, files in os.walk(path):
        # 按文件名排序
        files=natsorted(files)
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载视频
                video = VideoFileClip(filePath)
                # 添加到数组
                L.append(video)

    # 拼接视频
    final_clip = concatenate_videoclips(L)

    # 生成目标视频文件
    final_clip.to_videofile(r"{}/target.mp4".format(path), fps=24, remove_temp=False)

def rename(path):
    count=1
    files=os.listdir(path)
    for i in files:
        sg.Print("重命名{}为{}".format(i,count))
        os.rename("{}/{}".format(path,i),"{}/{}.mp4".format(path,count))
        count=count+1

sg.theme('SandyBeach')

layout=[
        [sg.Text('正在读取的文件夹为:',font=("微软雅黑", 12)),sg.Text('',key='fold',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
        [sg.FolderBrowse("选择文件夹",target='fold',key='folder'),sg.Button("重命名"),sg.Button("执行"),sg.Button("备注"),sg.Button("关闭程序")]
       ]

window=sg.Window("合并视频",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    if event in ("执行"):
        path=values["folder"]
        combine_mp4(path)
    elif event in ("重命名"):
        rename(values["folder"])
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("重命名可以把文件夹中的文件名按照1,2,3等排序，出现卡顿是正常的，等一下即可")
window.close()
   
