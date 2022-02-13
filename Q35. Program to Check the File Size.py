#!/usr/bin/env python
# coding: utf-8

# #Program to Check the File Size

# In[13]:


#Example 1: Using os module


import os
file_stat = os.stat("C://Users//gguglani//Documents//DATA SCIENCE//PYTHON PROGRAMIZ PRACTICE//my_file.txt")
print(file_stat.st_size)


# Using stat() from the os module, you can get the details of a file. Use the st_size attribute of stat() method to get the file size.
# 
# The unit of the file size is byte.

# In[14]:


#Example 2: Using pathlib module

from pathlib import Path

file = Path("C://Users//gguglani//Documents//DATA SCIENCE//PYTHON PROGRAMIZ PRACTICE//my_file.txt")
print(file.stat().st_size)


# Using the pathlib module, you can do the same thing as shown above. The unit of the file size is byte
