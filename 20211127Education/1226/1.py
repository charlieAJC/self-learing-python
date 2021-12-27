# regex 宣告字串
# r"r[au]n" -> 匹配:ran, run
# r"黃[小小|小中|中大]明" -> 匹配:黃小小明, 黃小中明, 黃中大明
# r"黃[小中][明華]" -> 匹配:黃小明, 黃小華, 黃中明, 黃中華

import re
pattern = r"r[au]n"
text = 'dog runs to cat'
# 官方文件:https://docs.python.org/3/library/re.html#re.search
x = re.search(pattern, text)
print(x)

# regex參考影片: https://www.youtube.com/watch?v=l1MAW1z641E
# \d: 匹配所有數字
# \D: 匹配所有非數字(包含空白、換行符號...)

# \s: 匹配所有空白 [\t\n\r\f\v]
# -> \t: tab
# -> \n: 換行
# -> \r: 鍵盤 home 鍵
# \S: 匹配所有非空白

# \b: 吻合文字邊界
# -> https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide/Regular_Expressions#special-word-boundary
# -> https://stackoverflow.com/questions/17020224/difference-between-b-and-s-in-regular-expression
# \w: 英文字母大小寫、數字、_
# \d: 數字

# .: 任意字，不包含 \n

# ^: 開頭符號
# $: 結束符號

# *: 吻合 0 次到無限多次
# +: 吻合 1 次到無限多次
# {n}: 吻合 n 次
# {n, m}: 吻合 n ~ m 次
