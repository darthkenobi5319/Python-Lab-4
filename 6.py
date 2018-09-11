# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:29:26 2017

@author: ZHENGHAN ZHANG
"""
#define the list of lists
list_of_lists = [ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'] ]
m=''
#loop
for i in range(len(list_of_lists)):
    m=''
    print('+-'*len(list_of_lists[i]),'+',sep='')   
    for j in range(len(list_of_lists[i])):        
        m+='|'+list_of_lists[i][j]
    print(m,'|',sep='')    
print('+-'*len(list_of_lists[i]),'+',sep='')