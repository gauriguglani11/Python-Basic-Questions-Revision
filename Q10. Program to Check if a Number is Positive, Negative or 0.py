#!/usr/bin/env python
# coding: utf-8

# #Program to Check if a Number is Positive, Negative or 0

# In[41]:


num = float(input("enter the number you want to check"))

if num>0:
        print("number is positive")
elif num ==0:
    print("number is neutral")
else:
    print("number is negative")


# #Here, we have used the if...elif...else statement. 

# In[43]:


# We can do the same thing using nested if statements as follows.

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")

