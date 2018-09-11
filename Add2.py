# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:16:49 2017

@author: ZHENGHAN ZHANG
"""

#input the matrix
mtx = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print('Original matrix is: ')
#pretty print the matrix(see the codes before)
m=''
#loop
for i in range(len(mtx)):
    m=''
    print('+-'*len(mtx[i]),'+',sep='')   
    for j in range(len(mtx[i])):        
        m+='|'+str(mtx[i][j])
    print(m,'|',sep='')    
print('+-'*len(mtx[i]),'+',sep='')

#transpose the matrix
print('Transposed matrix is: ')

for i in range(len(mtx[i])):
    m=''
    print('+-'*len(mtx),'+',sep='')   
    for j in range(len(mtx)):        
        m+='|'+str(mtx[j][i])
    print(m,'|',sep='')    
print('+-'*len(mtx),'+',sep='')