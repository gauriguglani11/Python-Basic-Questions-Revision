#!/usr/bin/env python
# coding: utf-8

# #Program to Iterate Through Two Lists in Parallel

# In[15]:


list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)


# Using zip() method, you can iterate through two lists parallel as shown above.
# 
# The loop runs until the shorter list stops (unless other conditions are passed).
# 
# 

# Example 2: Using itertools (Python 2+)

# In[16]:


import itertools

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

# loop until the short loop stops
for i,j in zip(list_1,list_2):
    print(i,j)

print("\n")

# loop until the longer list stops
for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)


# Using the zip_longest() method of itertools module, you can iterate through two parallel lists at the same time. The method lets the loop run until the longest list stops.
