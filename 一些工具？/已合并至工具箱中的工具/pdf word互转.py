from pdf2docx import Converter
import re
from win32com.client import constants,gencache
 
# 传入文件绝对路径
def pdf_to_word(fileName):
    pdf_file = fileName
    # 正则获取不含文件类型后缀的部分，用于组成word文档绝对路径
    name = re.findall(r'(.*?)\.',pdf_file)[0]
    docx_file = f'{name}.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
def word_to_pdf(fileName):
    word=gencache.EnsureDispatch("Word.Application")
    wordPath=fileName
    name = re.findall(r'(.*?)\.',wordPath)[0]
    pdfPath=f'{name}.pdf'
    doc=word.Documents.Open(wordPath,ReadOnly=0)
    doc.ExportAsFixedFormat(pdfPath,constants.wdExportFormatPDF)
import PySimpleGUI as sg
import re
 
# 主题设置
sg.theme('DarkTeal7')
 
# 布局设置
layout = [
          [sg.Text('待转化的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
          [sg.Text('程序操作记录',justification='center')],
          [sg.Output(size=(80, 20),font=("微软雅黑", 10))],                
          [sg.FileBrowse('选择文件',key='file',target='filename'),sg.Button('开始转化'),sg.Button('关闭程序')]
         ]      
 
# 创建窗口
window = sg.Window('pdf,word互转工具', layout,font=("微软雅黑", 15),default_element_size=(50,1))    
 
# 事件循环
while True:
    event, values = window.read()
    if event in (None, '关闭程序'):
        break
    if event == '开始转化':
        if values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='pdf':
            print("正在从pdf转word")
            fileName = values['file']
            pdf_to_word(fileName)
            print('\n----------转化完毕----------\n')
        elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='docx':
            print("正在从word转pdf")
            fileName = values['file']
            word_to_pdf(fileName)
            print('\n----------转化完毕----------\n')
        elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='doc':
            print("正在从word转pdf")
            fileName = values['file']
            word_to_pdf(fileName)
            print('\n----------转化完毕----------\n')
        else:
            print(values['file'])
            print(re.findall(r'\.(\S+)',values['file'])[0])
            print('文件未选取或文件非pdf文件或非word文件\n请先选择文件')
 
window.close()