# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:47:06 2021

@author: kplis
"""


print('jak długi ma być ciąg ? n= ')
n=0
n=input()
l=int(n)
i=0
x=0
y=0
ciag=[]
for  i in range(l):
    print('podaj ',i+1,'liczbę w ciągu');
    x=input();
    y=int(x);
    ciag.append(y);
    i=i+1;
    
    
print('To jest twój ciąg:',ciag)


imax=1
b=0    
j=0

for m in range (0, l):
    print('L= ',l)
    
    for j in range(m + 1, l):
        
        if ciag[m] > ciag[j]:
            b = ciag[j]
            ciag[j] = ciag[m]
            ciag[m] = b
            
            print('To jest twój ciąg:',ciag)
        

        
print('To jest twój ciąg:',ciag)