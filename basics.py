#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:39:09 2019

@author: oaryeetey
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
"""
cvalues=[20.1,20.8,34.5,67]
c=np.array(cvalues)
print(c, type(c))

a=[[1,2,3,4],[5,6,7,8],[10,11,12,13]]
print(a)
a1=np.array(a)
print(a1)
b=np.arange(0,15,1)
print(b)
b_reshape=b.reshape(3,5)
print(b_reshape)


zeros=np.zeros((2,2))
print(zeros)
ones=np.ones((2,3))
print(ones)

line=np.linspace(0,3,9)
print(line)
x=np.linspace(0,2*m.pi,100)
f=np.sin(x)
print(x,f)
plt.plot(x,f)

d=np.arange(24).reshape(2,3,4)
#print(d)
#print(d[0,1,2])
x=np.array([20,30,40,50])
y=np.arange(1,5)
x=x.reshape(2,2)
y=y.reshape(2,2)
z=x.dot(y)

print(z) #elementwise product 
"""
b=np.arange(0,100,10)
c=np.arange(0,10)
print(b,c)
plt.plot(c,b)
coeffs=np.polyfit(c,b,1)
print(coeffs[0],coeffs[1])
y_line=