#!/usr/bin/env python
# coding: utf-8

# #Program to Find the Sum of Natural Numbers

# In[7]:


# Sum of natural numbers up to num

num = 2

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
    


# Note: To test the program for a different number, change the value of num.
# 
# Initially, the sum is initialized to 0. And, the number is stored in variable num.
# 
# Then, we used the while loop to iterate until num becomes zero. In each iteration of the loop, we have added the num to sum and the value of num is decreased by 1.
