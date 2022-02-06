#!/usr/bin/env python
# coding: utf-8

# #Program to calculate the area of triangle

# In[24]:


#formula of area of triangle is
# s = (a+b+c)/2
#area = √(s(s-a)*(s-b)*(s-c))

a=5
b=6
c=7
# To take inputs from the user refer below comments
#a = float(input('Enter first side: '))
#b = float(input('Enter second side: '))
#c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of the triangle is %0.2f' %area)


# #In the above program, we have calculated the area of a triangle using Heron's formula
