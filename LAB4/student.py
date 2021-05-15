# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:31:00 2021

@author: kplis
"""

class Student:

    def __init__ (self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__pesel = pesel            #zmienna prywatna
        self.ocena = 5
        
    def przedstaw_sie(self):
        print(f'jestem {self.imie}, {self.nazwisko}')
        
    def podajpesel(self):
        return self.__pesel
        
        
OBS1 = Student('Konrad', 'Pliszka', 12547892)
OBS2 = Student('Roman', 'Nowak', 2648423)

OBS1.przedstaw_sie()
OBS2.przedstaw_sie()
print('ocena studenta 1 =', OBS1.ocena)
OBS1.ocena= 4
print('ocena studenta 1 =', OBS1.ocena)
print('ocena studenta 2 =', OBS2.ocena)

pobranypesel = OBS1.podajpesel()
print('pesel:', pobranypesel)
pobranypesel = OBS2.podajpesel()
print('pesel:', pobranypesel)