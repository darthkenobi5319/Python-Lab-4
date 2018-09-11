# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:08:33 2017

@author: ZHENGHAN ZHANG
"""

import random

x=[]
for i in range(random.randint(1,11)):
    #a block of codes that generate the strings
    string=''
    for j in range(random.randint(3,9)):
        string+=chr(random.randint(97,122))
    x.append(string)
print(x)
for i in range(len(x)):
    print(x[i])


    
