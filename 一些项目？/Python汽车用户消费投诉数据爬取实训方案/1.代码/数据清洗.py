import pandas as pd
#去重加修改时间
data = pd.read_excel("information.xlsx",parse_dates=["时间"])
data = data.drop_duplicates(subset=["详细信息"],keep="first")
data.to_excel("pure.xlsx")
