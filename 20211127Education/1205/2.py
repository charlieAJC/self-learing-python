# # import 整個套件
# import pandas as pd
# import numpy as np
# # call function
# pd.a
# pd.b

# # 從套件中匯入單一 function ，常用在同時 import 兩套件，但有 function 名稱互相衝突
# from pandas import a as abc
# # call function
# abc

# 陣列第一層一定都是列，第二層一定都是欄

# --- 用 pandas 將二維資料轉換成表格 ---
# import pandas as pd

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = pd.DataFrame(x)
# # 指定 列 名稱
# y.index = ['北區', '中區', '南區']
# # 指定 欄 名稱
# y.columns = ['手機', '平板', '電腦']

# print(y)
# print(x)

# 利用字典(json)生成 dataframe
# --- 人口及土地面積 ---
# nan: not a number ， numpy 專有形態， python 表示為 NONE
# 深入研究:https://zhuanlan.zhihu.com/p/63148067
# import pandas as pd

# area_dict = {
#     'taipei': 38332521,
#     'taoyuang': 26448183,
#     'hsinchu': 19651127,
#     'taichung': 19552860,
#     'kaohsung': 12882135,
#     'tainan': 12882135,
# }
# population_dict = {
#     'taipei': 423967,
#     'taoyuang': 141297,
#     'hsinchu': 695662,
#     'taichung': 170312,
#     'kaohsung': 149995,
#     'janpan': 123456,
#     'china': 0,
# }
# states = pd.DataFrame({'population': population_dict, 'area': area_dict})
# print(states)

# 匯入 excel 並新增欄位
import pandas as pd

# 請注意路徑隨環境更改，且路徑符號是用"斜線"!
data1 = pd.read_excel("C:/Users/Administrator/Desktop/python/2330_211202.xlsx")
# 新增一列 忽視所有值
# 新增一列 append() 新增一欄 insert()
data1 = data1.append({}, ignore_index=True)
# 指定 列 名稱
data1.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
# 取欄位值
# 取單一格子的值
x = data1.loc['C', '均價']
# 取連續範圍格子的表
# dataframe 的範圍含頭含尾， python 是含頭不含尾
y = data1.loc['C':'G', '買賣超':'均價']
# 將單一格子填值
data1.loc['C', '均價'] = 606060
# numpy 輸出一律為浮點數，所以就算某欄位是整數 123 ， console 輸出會是 123.0

# 陣列索引負值取值:https://medium.com/@huang09730298/python-%E7%B4%A2%E5%BC%95%E4%B8%89%E5%85%A9%E4%BA%8B-%E7%B4%A2%E5%BC%95%E8%B2%A0%E5%80%BC-40f4ceb77206
a = data1.loc[:'J', '績效']
for i in a:
    print(i)

# aaa=a.sum()

# mysum=0
# for i in a:
#     mysum=mysum+i
myave = a.sum()/len(a)

print(data1.shape)  # ==>(11,5) ==> [11,5]
# row=data1.shape[0]
# col=data1.shape[1]
row, col = data1.shape  # 等同於上面兩行

data1.loc[data1.index[row-1], data1.columns[0]] = '平均'
data1.loc[data1.index[row-1], data1.columns[1]] = myave

# 新增一欄
data1.insert(2, column='五月', value=range(row))

# function iloc(欄位序號) 使用方法
# 欄列數字從 0 開始算， 2:6 含頭不含尾!
# 取第 2 ~ 5 欄，第 4 列的值
print(data1.iloc[2:6, 4])

# 刪除一欄表格
data1 = data1.drop(columns=[data1.columns[3]])
# 刪除一列
data1 = data1.drop(index=[data1.index[0]])
# 刪除連續列
data1 = data1.drop(index=data1.index[0:2])
# 匯出成 excel(csv 也可以)，也可以覆蓋舊的
data1.to_excel("C:/Users/Administrator/Desktop/python/2330_211202_export.xlsx")

# 任何數字與 pd.nan 運算結果都是 pd.nan ， 1 + pd.nan = pd.nan
# 如果資料其中一欄出現 pd.nan (案例:sensor 傳輸異常)，那麼平均就是 pd.nan
# 如何處理這個 pd.nan ? 案例: 10 筆資料出現 1 筆 pd.nan ，計算平均就不能除 10，應該要除 9
# 該如何處理這些細節? 這堂課只會教資料運算，不會教太多資料處理
