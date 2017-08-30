#-*- encoding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
#内层字典的键值会被合并、排序以形成最终的索引
pop = {'Nevada':{2001:2.4,2002:2.9},
       'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = DataFrame(pop)
#rint frame3
#Dataframe也有行和列有name属性，DataFrame有value属性
frame3.index.name = 'year'
frame3.columns.name = 'state'
# print(frame3)
print(frame3.values)