from PyPDF2 import PdfFileMerger
import os
file_dir = input("输入你所需要合并的pdfs所在的文件途径：")  #你的文件路径
def getFlist(path):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  #当前路径
        print('sub_dirs:', dirs)   #子文件夹
        print('files:', files)     #文件名称，返回list类型
    return files
pdfs = getFlist(file_dir)
print(pdfs)
merger=PdfFileMerger()
for pdf in pdfs:
    merger.append(file_dir+pdf)
name=input("输入合成后你想要的文件名字：")
merger.write("{}.pdf".format(name))
merger.close()
