# 算术运算符
# print(321 % 123)     # 求餘數运算
# print(321 // 123)    # 求商运算
# print(321 ** 123)    # 次方运算，左邊為321的123次方

# 赋值运算符和复合赋值运算符
# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 算一下这里会输出什么

# 比较运算符
# 比较运算符的优先级高于赋值运算符，所以flag0 = 1 == 1先做1 == 1产生布尔值True，再将这个值赋值给变量flag0
# python的==即為php的強等於(===)
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# # 驚嘆號不可獨立呈現，需用not
# flag5 = not (1 != 2)
# print('flag0 =', flag0)    # flag0 = True
# print('flag1 =', flag1)    # flag1 = True
# print('flag2 =', flag2)    # flag2 = False
# print('flag3 =', flag3)    # flag3 = False
# print('flag4 =', flag4)    # flag4 = True
# print('flag5 =', flag5)    # flag5 = False

# 運算符的例子
# 例子1：华氏温度转换为摄氏温度 C = (F - 32) / 1.8
f = float(input('請輸入華氏溫度： '))
c = (f - 32) / 1.8
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, c))
# 格式化字符串f-string 
# 參考連結：https://blog.csdn.net/sunxb10/article/details/81036693
print(f'{f:.1f}華氏溫度 = {c:.1f}攝氏溫度')