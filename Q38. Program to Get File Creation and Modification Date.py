#!/usr/bin/env python
# coding: utf-8

# #Program to Get File Creation and Modification Date

# In[21]:


#Example 1: Using os module

import os.path, time

file = pathlib.Path("C://Users//gguglani//Documents//DATA SCIENCE//PYTHON PROGRAMIZ PRACTICE//my_file.txt")
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))


# getmtime() gives the last modification time whereas getctime() gives the last metadata change time in Linux/Unix and path creation time in Windows.

# In[22]:


#Example 2: Using stat() method


import datetime
import pathlib

fname = pathlib.Path("C://Users//gguglani//Documents//DATA SCIENCE//PYTHON PROGRAMIZ PRACTICE//my_file.txt")
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))


# Similar to Example 1, st_mtime refers to the time of last modification; whereas, st_ctime refers to the time of the last metadata change on Linux/Unix and creation time on Windows.
