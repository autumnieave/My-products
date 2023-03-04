import PySimpleGUI as sg 
import time
import pandas as pd
 
def m(mon,note):
    rec_time = time.localtime()
    rec = "{}-{}-{}".format(rec_time.tm_year,rec_time.tm_mon,rec_time.tm_mday)
    old = pd.read_excel(r"C:\Users\黄健朗\Desktop\账本.xlsx")
    new_d = pd.DataFrame()
    o_d = list(old["日期"]) 
    o_d.append(rec)
    o_m = list(old["价格"])
    o_m.append(mon)
    o_n = list(old["备注"])
    o_n.append(note)
    o_mm = list(old["月份"])
    o_mm.append(rec_time.tm_mon)
    new_d["日期"] = o_d
    new_d["价格"] = o_m
    new_d["备注"] = o_n
    new_d["月份"] = o_mm
    new_d.to_excel(r"C:\Users\黄健朗\Desktop\账本.xlsx",index=False)
    sg.Print("-------------------------------------记录完成------------------------------------")
def co():
    rec_time = time.localtime()
    rec = "{}-{}-{}".format(rec_time.tm_year,rec_time.tm_mon,rec_time.tm_mday,rec_time.tm_hour,rec_time.tm_min,rec_time.tm_sec)
    old = pd.read_excel(r"C:\Users\黄健朗\Desktop\账本.xlsx")
    sg.Print("预计每日30元，每月小于1500元")
    sg.Print("本日 : {} ，剩余 : {}".format(old.loc[old["日期"]==rec]["价格"].sum(),30-old.loc[old["日期"]==rec]["价格"].sum()))
    sg.Print("本月 : {} ，剩余 : {}".format(old.loc[old["月份"]==rec_time.tm_mon]["价格"].sum(),1500-old.loc[old["月份"]==rec_time.tm_mon]["价格"].sum()))
sg.theme('SandyBeach')

layout=[
        [sg.Text("金额"),sg.Input(key="money",size=(15,1),text_color='blue')],
        [sg.Text("备注"),sg.Input(key="note",size=(15,1),text_color='blue')],
        [sg.Button("保存"),sg.Button("统计"),sg.Button("备注"),sg.Button("退出")]
       ]

window=sg.Window("账本",layout,font=("微软雅黑",15),default_element_size=(500,100))

while True:
    event,values=window.read()
    if event in (None,"退出"):
        break
    if event in ("保存"):
        m(values["money"],values["note"])
    if event in ("统计"):
        co()
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("这个是模板")
window.close()