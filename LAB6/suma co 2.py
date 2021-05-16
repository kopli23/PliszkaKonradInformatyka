# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:00:15 2021

@author: kplis
"""

X= [5,2,6,9,6,2,9]

suma = 0
i = 0
j=0
l=0
y=len(X)
l=int(y)

for j in range (l):
    suma = suma + X[i]
    print ('X = ', X[i])
    i=i+2;
    if i>l:
        break
    
print ('suma = ', suma)