# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 23:58:43 2022

@author: O-OUK
"""
import pandas as pd

#ex1
df = pd.read_csv("Automobile_data.csv")
print(df.head(5))
print(df.tail(5))
#ex3
d =df["price"].max()
print(df["company"][df['price']==d])
#ex4
print(df[df["company"]=='toyota'])
#ex5
print(df.groupby(['company'])["company"].count())
#ex6
print(df.groupby(["company"])['price'].max())
#ex7
print(df.groupby(["company"])['average-mileage'].mean())
#ex8
print(df.sort_values(by='price', ascending = False))
#ex9
GermanCars = [ ('Ford',23845) ,('Mercedes',171995) ,('BMV', 135925), ('Audi', 71400)]
japaneseCars = [('Toyota', 29995),('Honda',23600),('Nissan',61500 ),('Mitsubishi',58900)]
data=pd.DataFrame(GermanCars,columns=('company','price'))
data1=pd.DataFrame(japaneseCars,columns=('company','price'))











