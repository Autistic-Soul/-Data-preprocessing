# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:46:04 2018

@author: User
"""

#调整数据尺度
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
#导入数据
a = 'data.csv'
b = ['1','2','3','4']
data = read_csv(a, names = b)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:3]
Y = array[:, 3]
transformer = MinMaxScaler(feature_range = (0,1))
#数据转换
newX = transformer.fit_transform(X)
#设定数据的打印格式
set_printoptions(precision = 3) #‘3’控制小数点后多少位，此处是3位
print(newX)