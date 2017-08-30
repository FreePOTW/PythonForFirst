#-*- encoding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Series可以设置index，有点像字典，用index索引
obj = Series([1,2,3],index=['a','b','c'])
# print(obj['a'])

#也就是说，可以用字典直接创建Series
dic = dict(key = ['a','b','c'],value = [1,2,3])
dic = Series(dic)

#下面注意可以利用一个字符串更新键值
key1 = ['a','b','c','d']

#注意下面的语句可以将 Series 对象中的值提取出来，不过要知道的字典是不能这么做提取的
dic1 = Series(obj,index = key1)
# print(dic)
# print(dic1)

#isnull 和  notnull 是用来检测缺失数据
print(pd.isnull(dic1))

#Series很重要的功能就是按照键值自动对齐功能
dic2 = Series([10,20,30,40],index = ['a','b','c','e'])
# print(dic1 + dic2)

#name属性,可以起名字
dic1.name = 's1'
dic1.index.name = 'key1'
#Series 的索引可以就地修改
dic1.index = ['x','y','z','w']