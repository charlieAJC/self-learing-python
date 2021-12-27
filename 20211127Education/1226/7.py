import re

text = '''
<p>
    如題阿

    為何台灣加油站特~~別的密集?

    是因為人云亦云 喜歡油加個 100 300  或是一半

    負重比較輕 油耗比較漂亮?
</p>
'''

pattern = "[\w\W]*"
x = re.findall(pattern, text)
print(x)

# @todo ?s 好像是 java 的寫法
y = re.findall(r"<p>((?s).*)</p>", text)
print(y)
