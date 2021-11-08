# 變數命名
# 硬性規則
# 1.變數名稱由字母、數字和下劃線組成，數字不能當開頭
# 2.大小寫敏感，大寫A和小寫a是不同的變數
# 3.變數名不要跟Python语言的关键字（有特殊含义的单词，后面会讲到）和保留字（如已有的函数、模块等的名字）发生重名的冲突
# 非硬性規則
# 1.變數通常用小寫英文字母，多個單字間用下劃線連接

# 使用type()检查變數的类型
a = 100
b = 12.345
c = 'hello'
# python的布林值第一個字母是大寫
d = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>
print(type(d))    # <class 'bool'>

# 類型轉換
# 註：這並不會改變變數本身的型態
a = 100
b = 12.345
c = 'hello'
d = True
# 整数转成浮点数
print(float(a))    # 100.0
# 浮点型转成字符串
print(str(b))      # 12.345 (输出字符串时不会看到引号哟)
# 字符串转成布尔型
print(bool(c))     # True (有内容的字符串都会变成True)
# 布尔型转成整数
print(int(d))      # 1 (True会转成1，False会转成0)
# 将整数变成对应的字符
print(chr(97))     # a (97刚好对应字符表中的字母a)
# 将字符转成整数
print(ord('a'))    # 97 (Python中字符和字符串表示法相同)