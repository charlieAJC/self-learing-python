# README #

紀錄學習 Python 寫的 code

### Comments Style ###

[參考資料](https://www.askpython.com/python/python-comments)

```
# {Function Short Description}
# {Input Arguments {type} details}
# {Return {type} details}
# {Exception Details}
def add_numbers(numbers):
    sum_numbers = 0
    for num in numbers:
        sum_numbers += num
    return sum_numbers
```

### Python 物件導向包裝機制 ###

[Python的包裝機制 — Function, Class, Module, Package](https://medium.com/%E5%AE%85%E7%94%B7%E9%9B%9C%E5%AD%B8%E7%AD%86%E8%A8%98/python%E7%9A%84%E5%8C%85%E8%A3%9D%E6%A9%9F%E5%88%B6-function-class-module-package-29bd8defb20e)

注意：Class 中每個 Function 就算不帶參數也要帶一個參數 `self`
这是因为“每个与类相关联的方法调用都自动传递实参self ， 它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。”
[Python 错误之函数takes 0 positional arguments but 1 was given](https://blog.csdn.net/u014128608/article/details/78292852)

### Python 在不同層級目錄 import 模組的方法 ###
[參考資料](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/369650/)

### 有某行程式不想要 pep8 幫忙 format ###
目前有碰到的狀況
```
import sys
sys.path.append("..")
import database.database as database
```
`import database.database` 是自己做的套件，如需要在不同層級 import，需要使用 `sys.path.append("..")` 才能成功 import，但是 pep8 會自動 format 成以下順序
```
sys.path.append("..")
import sys
import database.database as database
```
如果不想被 pep8 修改順序，可以在 `import database.database` 尾端加入 `# noqa`
[參考資料](https://stackoverflow.com/questions/36827962/pep8-import-not-at-top-of-file-with-sys-path)