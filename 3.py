# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:25:21 2017

@author: ZHENGHAN ZHANG
"""
#from functools import reduce
#define the list
list_of_lists = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ], [ 10, 11, 12 ]]
x=0
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        x+=1
print(x)
#create the sublist
x=[]
for i in range(len(list_of_lists)):
    product=1
    for j in range(len(list_of_lists[i])):
        product *= list_of_lists[i][j]
    x.append(product)
print(x)    


#find the product sublist
#print(list(map(lambda x: reduce(lambda x,y: x*y, list_of_lists), range(len(list_of_lists)))))