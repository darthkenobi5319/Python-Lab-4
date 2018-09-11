# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:58:43 2017

@author: ZHENGHAN ZHANG
"""
#RANDOMIZATION OF EXERCISE 3, FOR EXAMPLE
import random

#define the list with random sublists (1-10)
n=random.randrange(1,11)
m=random.randrange(1,11)
x=[]
list_of_lists =[]

for i in range(n):
    for j in range(m):
        x.append(random.uniform(1, 10))
    list_of_lists.append(x)
    
#list_of_lists = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ], [ 10, 11, 12 ]]








#The Original Code should work without alternation!!!!!!! :)
a=0
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        a+=1
print(a)
#create the sublist
s=[]
for i in range(len(list_of_lists)):
    product=1
    for j in range(len(list_of_lists[i])):
        product *= list_of_lists[i][j]
    s.append(product)
print(list_of_lists)
print(s)    