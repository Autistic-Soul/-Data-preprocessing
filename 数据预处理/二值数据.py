# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:20:24 2018

@author: User
"""

#使用值将数据转化为二值，大于阈值设置为1，小于阈值设置为0
#该过程被称为二分数据或阈值转换
#在生成明确值或特征工程增加属性的时候使用
#二值数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer
#导入数据
a = 'data.csv'
b = ['1','2','3','4','5']
data = read_csv(a , names = b)
#将数据分为输入数据和输出结果
array = data.values
X = array[:, 0:4]
Y = array[:, 4]
transformer = Binarizer(threshold = 0.0).fit(X)
#数据转换
newX = transformer.transform(X)
#设定数据的打印格式
set_printoptions(precision = 3)
print(newX)