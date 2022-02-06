#!/usr/bin/env python
# coding: utf-8

# # Program to add two numbers

# In[3]:


# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Show the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# # Add Two Numbers With User Input
# 

# In[ ]:


#store input numbers
num1 = input("enter the 1st number: ")
num2 = input("enter the 2nd number: ")

#add two numbers
sum = float(num1) + float(num2)

#show the sum
print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))


# #concept of formating
# #Syntax : { } .format(value)
# 
# Parameters : 
# (value) : Can be an integer, floating point numeric constant, string, characters or even variables.
# 
# Returntype : Returns a formatted string with the value passed as parameter in the placeholder position.
