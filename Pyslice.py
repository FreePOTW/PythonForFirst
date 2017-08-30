"""
格式：  li[start : end : step]
start是切片起点索引，end是切片终点索引，但切片结果不包括终点索引的值。step是步长默认是1。
范例：http://www.cnblogs.com/lulipro/p/5052619.html
"""


testStr = '1234567890abcdefghijklmnopqrstuvwxyz';
print("---------------------------------------------------------------------------------------------")

# print(testStr[0:3])

print(testStr[:-5])


print(testStr[:-5:-1])


print(testStr[:-5:-3])