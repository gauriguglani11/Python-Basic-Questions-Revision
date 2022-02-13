#!/usr/bin/env python
# coding: utf-8

# #Python Program to Convert Bytes to a String

# In[12]:


print(b'Easy \xE2\x9C\x85'.decode("utf-8"))


# Using decode(), you can convert bytes into string. Here, we have used utf-8 for decoding. \xE2\x9C\x85 is the utf-8 code for ✅.

# Syntax : decode(encoding, error)
# 
# Parameters :
# encoding : Specifies the encoding on the basis of which decoding has to be performed.
# 
# error : Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and ‘ignore’ ignores the errors occurred.
# 
# Returns : Returns the original string from the encoded string.
