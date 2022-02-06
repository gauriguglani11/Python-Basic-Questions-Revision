#!/usr/bin/env python
# coding: utf-8

# #Program to Convert Kilometers to Miles

# In[37]:


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# #this value is stored in the kilometers variable
# 
# 1 kilometer is equal to 0.621371 miles, we can get the equivalent miles by multiplying kilometers with this factor.
# 
# kilometers = miles / conv_fac
