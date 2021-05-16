# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:37:25 2021

@author: kplis
"""

print('podaj wartosc graniczna ujemna= ')
min =0
min =input()
minint=int(min)
    
print('podaj wartosc graniczna dodatnia= ')
max =0
max =input()
maxint=int(max)

print('twoj ciag zaawiera sie od', minint,'do',maxint)

l=maxint-minint
print('l= ',l)

i=0
ciag=[]
y=minint
for  i in range(l):
    print('y= ',y)
    ciag.append(y);
    print('y= ',y)
    y=y+1
    i=i+1
    print('i= ',i)
    
    
print('ciag= ',ciag)

j=0
parzyste=[]
for j in range(l):
    if ciag[j]%2:
        z=ciag[j-3
               ]
        ciag.append(z);
        j=j+1
        
print('parzyste= ',parzyste)
            
"""
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
"""