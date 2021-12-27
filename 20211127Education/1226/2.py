import re

# password=input("設定你的密碼:")
password = "GHFgg54J~~GFJHGFJ"

# 資料檢查
password = password.strip()

# 中間不能有空白
if re.search(r"\s", password) != None:
    print('密碼內不能有空白,tab,enter')
# 密碼最小8字
elif len(password) < 8:
    print("長度必須最小為8字元")
# 密碼最多20字
elif len(password) > 20:
    print("長度必須小於20字元")
# 要有大寫
elif re.search(r"[A-Z]", password) == None:
    print("密碼內必須要有大寫字元")
# 要有小寫
elif re.search(r"[a-z]", password) == None:
    print("密碼內必須要有小寫字元")
# 要有數字
elif re.search(r"\d", password) == None:
    print("密碼內必須要有數字")
# 要有特殊符號 -> 鍵盤上有的特殊符號都包括(但其實還有更多)
elif re.search(r"[~@#$%^&*()+|}{?><\"\:\\\]\[';/.,]", password) == None:
    print("密碼內必須要有特殊符號")
else:
    print("通過檢查")
