#!/usr/bin/env python
# coding: utf-8

# # Program to find the square root`

# In[17]:


#code for postive numbers

# Note: change this value for a different result
num = 8 

# To take the input from the user
num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.1f is %0.1f'%(num ,num_sqrt))

#print('The square root ofnum is:',num_sqrt)


# #the 2nd print statement if we execute this will give all the outcomes after decimal, but if we want only specific numbers after decimal then we will be using the 1st print statement.
# 
# so as we can see I have applied 0.1%f which means only one digit after decimal(0.1*100=10)
# 
# In the same way for 2 digits after deicmal, we will mention 0.2%f.
# 
# 

# In[21]:


#For real or complex numbers

#finding the square root of real or complex numbers

#importing the complex math module
#Python has a built-in module that you can use for mathematical tasks for complex numbers which is called as cmath.
import cmath

#num = 1+ 2j

# To take input from the user
num = eval(input('Enter a number:'))

#cmath.sqrt() is used to find the square root of the complex no.
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))


# #Note: If we want to take complex number as input directly, like 3+4j, we have to use the eval() function instead of float().
# 
# The eval() method can be used to convert complex numbers as input to the complex objects in Python. 
