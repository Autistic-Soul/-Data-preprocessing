# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:11:15 2018

@author: User
"""

#对使用权重输入的神经网络和使用距离的K近邻算法的准确度的提升有显著作用
#标准化数据
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Normalizer
#导入数据
a = 'data.csv'
b = ['1','2','3','4','5']
data = read_csv(a ,names = b)
#将数据分为输入数据和输出结果
array = data.values
X = array[:,0:4]
Y = array[:, 4]
transformer = Normalizer().fit(X)
#数据转换
newX = transformer.transform(X)
set_printoptions(precision = 3) #‘3’控制小数点后多少位，此处是3位
print(newX)