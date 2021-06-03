from pandas import DataFrame

from numpy import nan as NA

import pandas as pd

#创建两个DataFrame对象

data1 = [[2.6,0.3,25],[20.2,NA, NA]]

df1=DataFrame(data1,index=['米饭','牛肉'],columns=['蛋白质','脂肪','碳水化合物'])

data2 = [[NA, 10.1, 1.4],[3, 3.2, 3.4]]

df2 = DataFrame(data2,index=['鸡蛋','牛奶'],columns=['蛋白质','脂肪','碳水化合物'])

#将df2中内容与df1内容合并

df1 = pd. 【1】([df1,df2])

print ('df1=:\n', df1)

#判断df1每一列中是否存在空值，并打印输出判断结果（True或者False）

is_NAN = df1. 【2】().any()

print ('df1中是否有空值：\n', is_NAN)

#删除数据项缺失数量（有空值）大于等于2的行

df3 = df1.dropna(thresh = 【3】)

print ('df3 =:\n',df3)

#用列均值填充相应的缺失数据（原位修复）并打印输出修复后数据

df3.fillna({'蛋白质':df3['蛋白质'].mean()}, 【4】 = True )

print ('df3 =:\n',df3) 