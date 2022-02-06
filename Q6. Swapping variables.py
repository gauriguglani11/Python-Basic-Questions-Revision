#!/usr/bin/env python
# coding: utf-8

# #Program to swap two variables using Temporary variables

# In[29]:


# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# #Program to swap two variables without using Temporary variables

# In[30]:


x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

