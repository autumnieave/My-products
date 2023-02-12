
def combine_txts(path,result_name):
    filenames=os.listdir(path)
    result=r"D:\{}.txt".format(result_name)
    file=open(result,'w+',encoding='utf-8')
    for i in range(len(filenames)):
        print("正在合并{}.txt".format(i+1))
        for line in open(r"{}/{}.txt".format(path,i+1),encoding='utf-8'):
            file.writelines(line)
        file.write('\n')
    file.close
print("备注：为确保文件合并的有序性，请按序号编排，文件名必须为1.txt,2.txt等等")
path=input("请输入需要合并的txt文件所在的路径： ")
result_name=input("请输入合成后的文件名字： ")
combine_txts(path,result_name)



