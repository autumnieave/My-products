import pandas as pd
#去重
data = pd.read_excel("information.xlsx")
data = data.drop_duplicates(subset=["详细信息"],keep="first")
#修改日期格式
#改日期
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
count = 0
for i in data["时间"]:
    if i.find("-") == -1:
        #日
        ind_day = i.find(",")
        day = i[4:ind_day]
        #月
        for j in range(12):
            if i[:3] == months[j]:
                month = j+1
        #年
        year = i[ind_day+1:ind_day+6]
        #时间
        if i[-2] == "P":
            ind_hour = i.find(":")
            hour = int(i[ind_day+6:ind_hour])
            hour += 12
            time = i[ind_hour+1:-3]
            right = "{}".format(year)+"-"+"{}".format(month)+"-"+"{}".format(day)+" "+"{}".format(hour)+":"+time
        else:
            ind_hour = i.find(":")            
            hour = int(i[ind_day+6:ind_hour])
            time = i[-8:-3]
            right = "{}".format(year)+"-"+"{}".format(month)+"-"+"{}".format(day)+" "+"{}".format(hour)+":"+time
        data["时间"][count] = right[1:]
        count += 1
    elif i[3].isdigit()==False: 
        print(i)
        for j in range(12):
            if i[3:6] == months[j]:
                month = j+1
        time = i[12:]
        right = "{}-{}-{} ".format(i[7:11],month,i[:2])+time
        data["时间"][count] = right
        print(right)
        count += 1
    else:
        count += 1
data.to_excel("pure.xlsx")
