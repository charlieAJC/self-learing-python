# if statement
# tab 鍵不等於空白鍵，所以 4 個空白 != 1 個 tab 鍵，沒有錯只是因為編譯器幫忙轉換了
# true 和 false 的作用域界定: tab 鍵
# else if 在 python 用 elif 表示
a = 1
b = 2
if a > b:
    print('a 大於 b')
else:
    print('a 小於 b')
print('程式結束')

score = 99
if score >= 90:
    print('非常好')
elif score >= 80:
    print('很好')
elif score >= 70:
    print('及格')
elif score >= 60:
    print('輔導')
else:
    print('不及格，再見')

# 練習:BMI
height = 1.74
weight = 82
# rount() 取小數點以下幾位
# https://www.delftstack.com/zh-tw/howto/python/how-to-round-to-two-decimals-in-python/
bmi = round(weight / height ** 2, 2)
print(f'BMI: {bmi}')
if bmi >= 35:
    print('重度肥胖')
elif bmi >= 30:
    print('中度肥胖')
elif bmi >= 27:
    print('輕度肥胖')
elif bmi >= 24:
    print('過重')
elif bmi >= 18.5:
    print('正常範圍')
else:
    print('體重過輕')
