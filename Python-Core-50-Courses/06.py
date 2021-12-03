# 1 ~ 100求和
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# range(101)        : 會取 0 ~ 100 之間的整數，注意不會取到 101
# range(1, 101)     : 會取 1 ~ 100 之間的整數，1是開頭101是(不包含)結尾
# range(1, 101, 2)  : 會取 1 ~ 100 之間的整數，遞增值為 2
# range(100, 0, -2) : 會取 100 ~ 0 之間的整數，遞減值為 2

# 1 ~ 100之间的偶数求和
# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)

# 1 ~ 100 猜數字，並記錄猜的次數
# import random
# # 注意，randint(1, 100) 會隨機取 1(包含) 到 100(包含) 的整數，不要和 range() 搞混了！
# answer = random.randint(1, 100)
# # print(f'答案是 {answer}')
# counter = 0
# while True:
#     counter += 1
#     # 注意 input() 回傳參數型態是 string ，需轉成 integer 才能比較
#     guess = int(input('請輸入 1 到 100 間的數字： '))
#     if (guess > answer):
#         print('太大了❤')
#     elif (guess < answer):
#         print('好小喔')
#     else:
#         print('❤❤❤中了❤❤❤')
#         break
# print(f'總共猜了 {counter} 次')

# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end = '\t')
    print()