# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:31:33 2023

@author: Pc
"""

a=[]
n=int(input("enter the no.of elements you update :"))
for i in range(0,n):
    c=input("enter the eleents:")
    a.append(c)
b=input("enter the string to find the frequency:")
x=0
for j in a:
    if j==b:
        x+=1
print("the frquency of",b,"is",x)
    