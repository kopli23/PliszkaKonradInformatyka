# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def nazwafunkcji():
    print('cialo funkcji')
   
def funkcjazargumentem(zmienna):
        print('podałes zmienną = ', zmienna)
def silnia(n):
    silnia = 1
    i = 1
 
    for i in range(1,n+1,1):
        silnia = silnia * i
        print('silnia for: ',silnia)
    
nazwafunkcji()
funkcjazargumentem(10)
silnia(5)
silnia(7)
