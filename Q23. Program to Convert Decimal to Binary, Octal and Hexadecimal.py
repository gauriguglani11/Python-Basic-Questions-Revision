#!/usr/bin/env python
# coding: utf-8

# #Program to Convert Decimal to Binary, Octal and Hexadecimal

# A number with the prefix 0b is considered binary, 0o is considered octal and 0x as hexadecimal. For example:
# 
# 60 = 0b11100 = 0o74 = 0x3c

# In[1]:


# Python program to convert decimal into other number systems
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In this program, we have used built-in functions bin(), oct() and hex() to convert the given decimal number into respective number systems.
# 
# These functions take an integer (in decimal) and return a string.
