#!/usr/bin/env python
# coding: utf-8

# #Program to Get the Full Path of the Current Working Directory

# In[18]:


import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())


# Using the pathlib module, you can get the current working directory.
# 
# Pass the file's name in Path() method.
# 
# parent gives the logical parent of the path and absolute() gives the absolute path of the file.
# 
# pathlib.Path().absolute() gives the current working directory.

# In[19]:


#Example 2: Using os module

import os

# path of the given file
print(os.path.dirname(os.path.abspath("my_file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))


# You can do the same thing with the os module.
# 
# Use abspath() method to get an absolute path.
# getcwd() gives the current working directory.
# 
