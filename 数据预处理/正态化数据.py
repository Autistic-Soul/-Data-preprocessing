# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:04:49 2018

@author: User
"""

#正态化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler
#导入数据
a = 'data.csv'
b = ['1','2','3','4','5']
data = read_csv(a ,names = b)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:4]
Y = array[:, 4]
transformer = StandardScaler().fit(X)
#数据转换
newX = transformer.transform(X)
#设定数据的打印格式
set_printoptions(precision = 3) #‘3’控制小数点后多少位，此处是3位
print(newX)