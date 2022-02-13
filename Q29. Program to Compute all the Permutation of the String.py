#!/usr/bin/env python
# coding: utf-8

# #Program to Compute all the Permutation of the String

# 1. Permutation is the method of selecting elements from a set in different ways.
# 
# 2. For example: the number of ways in which characters from yup can be selected are yup, ypu, uyp, upy, puy, pyu, and not selecting any.

# In[28]:


def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('yup'))


# In this example, recursion is used to find the permutations of a string yup.
# 
# The if condition prints string passed as argument if it is equal to the length of yub.
# 
# In each iteration of the for loop, each character of yup is stored in words.
# 
# The elements of words are swapped. In this way, we achieve all different combinations of characters.
# 
# This process continues until the maximum length is reached.

# Example 2: Using itertools

# In[29]:


from itertools import permutations

words = [''.join(p) for p in permutations('pro')]

print(words)


# Using permutations from itertools module, we can find the permutations of a string.
# 
# 
