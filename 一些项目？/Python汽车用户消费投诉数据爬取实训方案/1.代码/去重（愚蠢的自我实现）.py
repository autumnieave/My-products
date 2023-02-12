data = pd.read_excel("information.xlsx")
data["详细信息"].value_counts().rename_axis("value").to_frame("count").to_excel("重复的数据.xlsx")
datas = pd.read_excel("重复的数据.xlsx")
count = 0
for i in datas["count"]:
    if int(i) > 1:
        count += 1
datas = datas.iloc[:count]
count_ls = []
for i in datas["count"]:
    count_ls.append(i)
ind = 0
for j in data["详细信息"]:
    indd = 0
    for i in datas["value"]:
        if i == j: 
            count_ls[indd] -= 1   
            if count_ls[indd] != 0:
                data = data.drop(index = ind)
                print("清除，内容为:{}".format(i[:5]))
        indd += 1
    ind += 1
data["详细信息"].value_counts().rename_axis("value").to_frame("count").to_excel("重复的数据.xlsx")
datas = pd.read_excel("重复的数据.xlsx")
data.to_excel("pure.xlsx")
data = pd.read_excel("pure.xlsx")
for i in datas["count"]:
    if int(i) > 1:
        count += 1
datas = datas.iloc[:count]
ind = 0
for j in data["详细信息"]:
    indd = 0
    for i in datas["value"]:
        if i == j: 
            count_ls[indd] -= 1   
            if count_ls[indd] != 0:
                data = data.drop(index = ind)
                print("清除，内容为:{}".format(i[:5]))
        indd += 1
    ind += 1
data["详细信息"].value_counts().rename_axis("value").to_frame("count").to_excel("重复的数据.xlsx")
datas = pd.read_excel("重复的数据.xlsx")
