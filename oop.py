# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 17:55:54 2022

@author: O-OUK
"""
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self.age=age
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

class Numbers:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        s=x+y
        self.somme=s
    def multiply(a):
        return a*2
    def subtract(b,c):
        return b-c
    @property
    def value(self):
        return '{} , {}'.format(self.x,self.y)
        
    @value.setter
    def value(self,xy):
        x,y=xy.split(' , ')
        self.x=x
        self.y=y
    @value.deleter
    def value(self):
        print('delete x and y')
        self.x=None
        self.y=None
