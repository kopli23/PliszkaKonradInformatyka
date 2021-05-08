# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:24:58 2021

@author: kplis
"""

A=5
B=10

suma=0
i=0

print ('A =',A)
print ('i =',i)
print ('suma =',suma)
while A <= B:
    R=A%2
    if R!=0:
        suma=suma+A;
        A=A+1;
        i=i+1;
        print ('A =',A-1,' jest to liczba nieparzysta')
        print ('R =',R)
        print ('i =',i)
        print ('suma =',suma)
    else:
        A=A+1;
        print ('A =',A-1,' jest to liczba parzysta')
        print ('R =',R)
s=suma/i;
print ('srednia =',s)