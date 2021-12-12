# 匯入 excel 並新增欄位
import pandas as pd

# 請注意路徑隨環境更改，且路徑符號是用"斜線"!
# sheet_name 可以指定要 excel 中的哪個工作表
data1 = pd.read_excel("C:/Users/Administrator/Desktop/python/2330_211202.xlsx")

# # value 型態可以混用，但各個 key 包含的參數量一定要一致
# data2 = pd.DataFrame({
#     '券商分點': 1,
#     '績效': [2],
#     '總損益(仟)': [3],
#     '買賣超': [4],
#     '均價': [5]
# })
# # 將兩筆數據合併
# # ignore_index:忽略合併時舊的 index 欄位，改採用自動產生的 index
# dataAppend = data1.append(data2, ignore_index=True)

# mean() 取欄位平均
# 指定一列取平均，若沒有指定列，會自動確定哪些列適合應用 mean() 功能
performance_average = data1['績效'].mean()
dataAppend = data1.append(data1.mean(), ignore_index=True)
