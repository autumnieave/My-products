import PySimpleGUI as sg 
import re
import os
from win32com.client import constants,gencache
from pdf2docx import Converter
from PyPDF2 import PdfFileMerger
import fitz, time
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup

def rename(path):
    files=os.listdir(path)
    type=files[0][files[0].find("."):]
    sg.Print("格式为{}".format(type))
    count=1
    files=os.listdir(path)
    for i in files:
        sg.Print("重命名{}为{}".format(i,count))
        os.rename("{}/{}".format(path,i),"{}/{}.{}".format(path,count,type))
        count=count+1

#轻小说爬取
def Pa_hjl(url_index,url):
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    rq_1=requests.get(url_index,headers=header)
    rq_1.encoding='gbk'
    html=rq_1.text
    bes=BeautifulSoup(html,"lxml")
    texts=bes.find("table", border="0")
    chapters = texts.find_all("a") 
    words = []
    for chapter in chapters:
        name = chapter.string 
        url1 = url + chapter.get("href")
        word = [url1, name] 
        words.append(word)
    target = words
    i=1
    for tar in target:
        sg.Print("正在爬取第{}个：{}".format(i,tar[1]))
        req = requests.get(url=tar[0],headers = header)
        req.encoding = 'gbk'
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("div", id = "content")
        texts_list = texts.text.split("\xa0"*4)
        req.close()
        with open("D:/novel/{}.txt".format(i),"w",encoding='utf-8') as file: 
            file.write(tar[1]+"\n")
            for line in texts_list:
                file.write(line+"\n")
        i=i+1

#图片转pdf
def pic_to_pdf(path):
    pdf=FPDF('P','mm','A4')#P竖，L横
    pl=path
    imagelist=[i for i in os.listdir(pl)]
    sg.Print(imagelist)
    for i in imagelist:
        pdf.add_page()
        pdf.image(pl+"/"+i,x=0,y=0,w=210,h=297)
    pdf.output(path+"/output.pdf","F")

#pdf合并
def combine_pdfs(path):
    def getFlist(path):
        for root, dirs, files in os.walk(path):
            sg.Print('root_dir:', root)  #当前路径
            sg.Print('sub_dirs:', dirs)   #子文件夹
            sg.Print('files:', files)     #文件名称，返回list类型
        return files
    pdfs = getFlist(path)
    sg.Print(pdfs)
    merger=PdfFileMerger()
    for pdf in pdfs:
        sg.Print("正在合并{}".format(pdf))
        merger.append(path+"/"+pdf)
    merger.write("{}/{}.pdf".format(path,"Combined_pdf"))
    merger.close()
    sg.Print("完成")

#txt合并
def combine_txts(path):
    filenames=os.listdir(path)
    result=r"{}\{}.txt".format(path,"合并后的txt")
    file=open(result,'w+',encoding='utf-8')
    for i in range(len(filenames)):
        sg.Print("正在合并{}.txt".format(i+1))
        for line in open(r"{}/{}.txt".format(path,i+1),encoding='utf-8'):
            file.writelines(line)
        file.write('\n')
    file.close
    sg.Print("已完成")

#提取pdf的图片
def pdf2pic(path):
    namee=""
    sg.Print(type(path))
    pic=path.split("/")
    for i in range(len(pic)-1):
        namee=namee+pic[i]+"/"
    namee=namee[:-1]
    sg.Print(type(namee))
    t0 = time.process_time()
    checkXO = r"/Type(?= */XObject)" 
    checkIM = r"/Subtype(?= */Image)" 
    doc = fitz.open(path)
    imgcount = 0
    lenXREF = doc.xref_length()
    sg.Print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))
    for i in range(1, lenXREF):
        text = doc.xref_object(i)
        isXObject = re.search(checkXO, text)
        isImage = re.search(checkIM, text)
        if not isXObject or not isImage:
            continue
        imgcount += 1
        pix = fitz.Pixmap(doc, i)
        new_name="{}.png".format(imgcount)
        if pix.n < 5:
            pix.save(os.path.join(namee,new_name))#注：此处与下面的os.path中的path并不是路径，而是os的一个函数，需要加路径则在join()内添加
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.save(os.path.join(namee,new_name))
            pix0 = None
        pix = None
        t1 = time.process_time()
        sg.Print("运行时间:{}s".format(t1 - t0))
        sg.Print("提取了{}张图片".format(imgcount)) 

#统计excel中的信息
def excel_sum(filename):
    sg.Print("我恨pandas")

#pdf转word
def pdf_to_word(fileName):
    pdf_file = fileName
    # 正则获取不含文件类型后缀的部分，用于组成word文档绝对路径
    name = re.findall(r'(.*?)\.',pdf_file)[0]
    docx_file = f'{name}.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

#word转pdf
def word_to_pdf(fileName):
    word=gencache.EnsureDispatch("Word.Application")
    wordPath=fileName
    name = re.findall(r'(.*?)\.',wordPath)[0]
    pdfPath=f'{name}.pdf'
    doc=word.Documents.Open(wordPath,ReadOnly=0)
    doc.ExportAsFixedFormat(pdfPath,constants.wdExportFormatPDF)

sg.theme('SandyBeach')  

layout = [
          [sg.Text('正在读取的文件是：',font=("微软雅黑", 12)),sg.Text('',key='filename',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
          [sg.Text('正在读取的文件夹为:',font=("微软雅黑", 12)),sg.Text('',key='fold',size=(50,1),font=("微软雅黑", 10),text_color='blue')],
          [sg.Text("小说的目录网页：",font=("微软雅黑", 12)),sg.InputText(key="url",size=(30,1)),sg.Button("开爬")],
          [sg.Button("备注"),sg.FileBrowse('选择文件',key='file',target='filename'),sg.FolderBrowse("选择文件夹",target='fold',key='folder'),sg.Button("重命名"),sg.Button('执行'),sg.Button('关闭程序')],
         ]      


window=sg.Window("工具箱",layout,font=("微软雅黑", 15),default_element_size=(500,100))


while True:
    event,values=window.read()
    if event in (None,"关闭程序"):
        break
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='xlsx':
        sg.Print("正在识别excel文件")
        fileName=values['file']
        excel_sum(fileName)
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='pdf':
        sg.Print("正在从pdf转word")
        fileName = values['file']
        pdf_to_word(fileName)
        sg.Print('\n----------转化完毕----------\n')
        sg.Print("正在从pdf提取图片")
        pdf2pic(values['file'])
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='docx':
        sg.Print("正在从word转pdf")
        fileName = values['file']
        word_to_pdf(fileName)
        sg.Print('\n----------转化完毕----------\n')
    elif values['file'] and re.findall(r'\.(\S+)',values['file'])[0]=='doc':
        sg.Print("正在从word转pdf")
        fileName = values['file']
        word_to_pdf(fileName)
        sg.Print('\n----------转化完毕----------\n')
    elif values['folder']:
        path=values['folder']
        file_names=os.listdir(path)
        if file_names[0].find("pdf")!=-1:
            sg.Print("识别文件中为pdf")
            combine_pdfs(path)
        elif file_names[0].find("txt")!=-1:
            sg.Print("识别文件中为txt")
            combine_txts(path)
        elif file_names[0].find("png")!=-1 or file_names[0].find("jpg")!=-1:
            sg.Print("识别文件中为图片，格式为jpg或png")
            pic_to_pdf(path)
        else:
            sg.Print("什么勾八文件夹，看看备注吧你")
    elif event in ("开爬"):
        url_index=values["url"]
        url=url_index[:-9]
        Pa_hjl(url_index,url)
        combine_txts(r"D:/novel")
    elif event in ("备注"):
        sg.Print("备注")
        sg.Print("本程序已实现：")
        sg.Print("1.pdf与word互转")
        sg.Print("2.txt文件与pdf文件的合并")
        sg.Print("3.pdf中图片的提取")
        sg.Print("4.多张图片转pdf")
        sg.Print("5.文库8的爬取(这个网站现在搞了个反爬的，有时候可以，有时候不行，随缘吧)")
        sg.Print("等，自行探索")
        sg.Print("此程序由初学者编写，如需联系请联系okura_machi@126.com")       
    else:
        sg.Print("你选了个啥玩意啊，看看备注吧你") 
window.close()