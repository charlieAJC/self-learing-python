# 自我練習 python 函數宣告
globvar = 0


def set_globvar_to_one():
    global globvar
    globvar = 1


def print_globvar():
    # 若 function 裡面沒有區域變數 globvar， python 會找有沒有全域變數 globvar
    print(globvar)


print_globvar()
set_globvar_to_one()
print_globvar()
