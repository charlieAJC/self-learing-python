# array取值
y = [2, 44, 99, 'a']
# 取特定索引
print(y[2])
# 取範圍索引
print(y[1:4])
# 從特定索引取到最後
print(y[2:])
# 從最初取到特定索引
print(y[:3])

# array賦值
y[2] = 'AAA'
print(y)
# # python 是少數可以範圍賦值的語言，但這種情況較少用到
y[1:3] = ['AAA', 'BBB', 'CCC', 'DDD'] # 1~3(3個位置)可以塞3個以上的資料! 也可以塞少於3個!
print(y)

# array刪除
del y[1]

# array新增值
y = [2, 44, 99, 'a']
y.append('huang') # 新增在array最後
print(y)
y.insert(1, 'chen') # 新增在指定位置
print(y)

# array merge 直接用 + 號!!
y = [2, 44, 99, 'a']
z = ['hsu', 'huang', 'chen']
a = ['ininder']
x = y + z + a
print(x)

# 資料型態 tuple :類似 array 但是不支援對內部參數的增刪修，從資料庫撈出來的資料常會是 tuple，資料範圍用小括號表示
# 可以將 tuple 以 list() 的方法強轉型態以修改其中的資料
# hihi = (1, 2, 3)

# 字典(dictionary)
x = ['chen', 23, '042345678', '台中市南屯區'] # 這是 array
y = {'age': 23, 'tel': '042345678', 'addr': '台中市南屯區', 'name': 'chen'} # 這是 dictionary
# array vs dict 的取值方法(重要!)
print(x[0])
print(y['name'])
# array vs dict 的賦值方法(重要!)
x.append('Male')
y['gender'] = 'Male'
print(x)
print(y)
# array vs dict 的刪值方法
del x[0]
del y['name']
print(x)
print(y)

# 逐筆 dict 加入 array
# 方法1.(較常使用)
arr = []
arr.append({'name': '陳小華', 'age': 33, 'tel': '042', 'addr': '台中市'})
arr.append({'name': '黃小芳', 'age': 25, 'tel': '047', 'addr': '彰化市'})
arr.append({'name': '吳小花', 'age': 28, 'tel': '022', 'addr': '新北市'})
arr.append({'name': '李小明', 'age': 27, 'tel': '035', 'addr': '新竹市'})
print(arr)
# 方法2.
# \ -> 接續符號，參數內容太長需換行用
# arr = [
#     {'name': '陳小華', 'age': 33, 'tel': '042', 'addr': '台中市'}, \
#     {'name': '黃小芳', 'age': 25, 'tel': '047', 'addr': '彰化市'}, \
#     {'name': '吳小花', 'age': 28, 'tel': '022', 'addr': '新北市'}, \
#     {'name': '李小明', 'age': 27, 'tel': '035', 'addr': '新竹市'}
# ]
# print(arr)