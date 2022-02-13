#!/usr/bin/env python
# coding: utf-8

# #Program to Check If Two Strings are Anagram

# A word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp is called as an Anagram

# In[48]:


str1 = input("enter string one ")
str2 = input("enter string two ")

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")


# We first convert the strings to lowercase. It is because Python is case sensitive (i.e. R and r are two different characters in Python).
# 
# Here,
# 
# lower() - converts the characters into lower case
# 
# sorted() - sorts both the strings
# 
# If sorted arrays are equal, then the strings are anagram.
