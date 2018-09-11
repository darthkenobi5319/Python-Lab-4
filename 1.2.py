# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:04:35 2017

@author: ZHENGHAN ZHANG
"""

#get the age from the user
x=int(input('Please enter your age: '))
#comparison
if 0<=x<=120:
    if 0<=x<=20:
        print('You are young!')
    else:
        if 20<x<=50:
            print('Middle aged!')
        else:
            if 50<x<=120:
                print('You are old!')
else:
    print('Out of range :(')