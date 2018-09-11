# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:11:13 2017

@author: ZHENGHAN ZHANG
"""
#define the list of lists
list_of_lists = [ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'] ]

#print1
m=0

        
for i in range(len(list_of_lists)):    
    for j in range(len(list_of_lists[i])):
        m+=1
        print('.'*(2*m-1),list_of_lists[i][j],sep='')  
    
#print2
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        print('.'*(2*i+1),list_of_lists[i][j],sep='')    