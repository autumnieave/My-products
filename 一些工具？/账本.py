import PySimpleGUI as sg 
import time
import pandas as pd
import calendar

def m(mon,note):
    new_day = False
    rec_time = time.localtime()
    rec = "{}-{}-{}".format(rec_time.tm_year,rec_time.tm_mon,rec_time.tm_mday)
    old = pd.read_excel(r"D:\账本.xlsx")
    new_d = pd.DataFrame()
    o_d = list(old["日期"]) 
    if rec != o_d[-1]:
        sg.Print("---------------------------------今天是新的一天！--------------------------------")
        new_day = True
    o_d.append(rec)
    o_m = list(old["价格"])
    o_m.append(mon)
    o_mm = list(old["月份"])
    o_mm.append(rec_time.tm_mon)
    o_n = list(old["备注"])
    o_n.append(note)
    o_o = list(old["赊账"])
    if new_day == False:
        left_money = o_o[-1] - int(mon)
        o_o.append(left_money)
    else:
        left_money = 30 + o_o[-1] - mon
        o_o.append(left_money)
        sg.Print("请注意，今天最好只花{}元".format(left_money))
    new_d["日期"] = o_d
    new_d["价格"] = o_m
    new_d["月份"] = o_mm
    new_d["备注"] = o_n
    new_d["赊账"] = o_o
    new_d.to_excel(r"D:\账本.xlsx",index=False)
    sg.Print("-------------------------------------记录完成------------------------------------")
def co():
    rec_time = time.localtime()
    rec = "{}-{}-{}".format(rec_time.tm_year,rec_time.tm_mon,rec_time.tm_mday,rec_time.tm_hour,rec_time.tm_min,rec_time.tm_sec)
    old = pd.read_excel(r"D:\账本.xlsx")
    sg.Print("预计每日30元，每周小于300元，每月小于1300元")
    sg.Print("本日 : {} ，剩余 : {}".format(old.loc[old["日期"]==rec]["价格"].sum(),list(old["赊账"])[-1]))
    sg.Print("本月 : {} ，剩余 : {} ".format(old.loc[old["月份"]==rec_time.tm_mon]["价格"].sum(),1300-old.loc[old["月份"]==rec_time.tm_mon]["价格"].sum()))
    sg.Print("本月还剩余{}天，平均每天可用 : {}".format(calendar.monthrange(rec_time.tm_year,rec_time.tm_mon)[1]-rec_time.tm_mday,(1300-old.loc[old["月份"]==rec_time.tm_mon]["价格"].sum())/(calendar.monthrange(rec_time.tm_year,rec_time.tm_mon)[1]-rec_time.tm_mday)))
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
        sg.Print("备注：请在D盘中创建一个名为账本的excel文件，并在第一行设置：日期，价格，月份，备注")
        sg.Print("本程序用于：")
        sg.Print("1.对每日的输出进行记录，内容在D盘中的名为账本的excel文件中。")
        sg.Print("2.对数据进行统计，对每日与每月的金额进行统计以及对这个月后期的金钱的规划。")
        sg.Print("本程序中的数据均可修改，如有需要联系的请发信息至okura_machi@126.com")
window.close()
