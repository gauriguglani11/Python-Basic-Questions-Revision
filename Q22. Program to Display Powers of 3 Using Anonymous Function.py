#!/usr/bin/env python
# coding: utf-8

# #Program to Display Powers of 3 Using Anonymous Function

# In[10]:


# Display the powers of 3 using anonymous function

terms = int(input("How many terms? ")) 

#using anonymous function
result = list(map(lambda x:  3** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("3 raised to power",i,"is",result[i])

