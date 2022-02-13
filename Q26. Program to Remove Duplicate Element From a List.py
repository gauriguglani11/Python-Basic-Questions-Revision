#!/usr/bin/env python
# coding: utf-8

# #Program to Remove Duplicate Element From a List

# In[13]:


list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))


# we first convert the list into a set, then we again convert it into a list. Set cannot have a duplicate item in it, so set() keeps only an instance of the item.

# # EX 2- Remove the items that are duplicated in two lists
# 
# 

# In[14]:


list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))


# In the above program we are trying  to remove duplicate from both the list and trying to print a totally unique list

# Firstly, both lists are converted to two sets to remove the duplicate items from each list.
# Then, ^ gets the symmetric difference of two lists (excludes the overlapping elements of two sets).
