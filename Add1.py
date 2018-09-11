# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 15:26:29 2017

@author: ZHENGHAN ZHANG
"""
#Using the code from the last practice



#process the coordinates entered by the user
l1=input('Please enter the first set of coordinates: ').split(',')
l2=input('Please enter the second set of coordinates: ').split(',')


#when it is entirely in column
if int(l1[0])==int(l2[0]):
    #integerize the numbers
    x=int(l1[1])
    y=int(l2[1])
    #reversible if entered(0,2)and(0,0)
    if x<=y:
        #repetition of three rows
        for i in range(3):
            m=''
            #print the decoration headings
            print('+-'*3,'+',sep='')  
            #generate every individual row by repeting the concatenation to empty string m
            for j in range(3):
                #counter which identifies whether this row would have an 'x'
                if x<=i<=y:
                    #identify where the 'x' would be in this row
                    if j==int(l1[0]):
                        m+='|'+'x'
                    else:    
                        m+='|'+' '
                #this is where a row has no 'x's      
                else:
                    m+='|'+' '
            print(m,'|',sep='')  
        #print the ending decoration line
        print('+-'*3,'+',sep='')
    else:
        for i in range(3):
            m=''
            print('+-'*3,'+',sep='')   
            for j in range(3):
                if y<=i<=x:
                    if j==int(l1[0]):
                        m+='|'+'x'
                    else:    
                        m+='|'+' '
                else:
                    m+='|'+' '
            print(m,'|',sep='')    
        print('+-'*3,'+',sep='')
#when it is entirely in rows
elif int(l1[1])==int(l2[1]):
    #integerize the indexes
    x=int(l1[0])
    y=int(l2[0])
    #reversibility considered
    if x<=y:
        #repetition of three rows to print
        for i in range(3):
            m=''
            #print the decorations(same as before)
            print('+-'*3,'+',sep='')
            #counter which identifies whether this column would have an 'x'
            if i==int(l1[1]):
            #generate every individual row by repeting the concatenation to empty string m
                for j in range(3):
                    #how many 'x's have you got？ :)
                    if x<=j<=y:
                        m+='|'+'x'
                    else:
                        m+='|'+' '                
            else:
                for j in range(3):
                    m+='|'+' '
            print(m)
    else:
        for i in range(3):
            m=''
            print('+-'*3,'+',sep='')
            if i==int(l1[1]):
                for j in range(3):                   
                    if y<=j<=x:
                        m+='|'+'x'
                    else:
                        m+='|'+' '                
            else:
                for j in range(3):
                    m+='|'+' '
            print(m)
        print('+-'*3,'+',sep='')
else:
    print('Error!Either the first or the second character of the coordinates must be the same!')