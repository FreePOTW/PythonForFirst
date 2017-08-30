#-*- encoding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#构建DataFrame可以直接传入等长的列表或Series组成的字典
#不等长会产生错误
data = {'a':[1,2,3],
        'c':[4,5,6],
        'b':[7,8,9]
}
#注意是按照列的名字进行列排序
frame = DataFrame(data)
# print(frame)
#指定列之后就会按照指定的进行排序
frame = DataFrame(data,columns=['a','c','b'])
# print(frame)
#可以有空列,index是说行名
frame1 = DataFrame(data,columns = ['a','b','c','d'],index = ['one','two','three'])
# print(frame1)
#用字典方式取列数据
# print(frame['a'])
# print(frame.b)
#列数据的修改直接选出来重新赋值即可
#行，可以用行名或者行数来进行选取
# print(frame1.ix['two'])
#为列赋值，如果是Series，规定了index后可以精确赋值
frame1['d'] = Series([100,200,300],index = ['two','one','three'])
# print(frame1)
#删除列用del 函数
del frame1['d']
#警告：通过列名选出来的是Series的视图，并不是副本，可用Series copy方法得到副本



pop = {'Nevada':{2001:2.4,2002:2.9},
       'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = DataFrame(pop)
print(frame3)