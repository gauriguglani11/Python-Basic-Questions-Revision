#!/usr/bin/env python
# coding: utf-8

# #Program to Count the Number of Occurrence of a Character in String

# In[23]:


count = 0

my_string = "GAURI GUGLANI"
my_char = "I"

for i in my_string:
    if i == my_char:
        count = count+1
print(count)
        


# WE CAN SEE IN THE ABOVE PROGRAM, ONLY CAPITAL LETTER WILL BE SEARCHED AS OUR STRING IS CAPITAL, SO THE NO. OF CHARACTERS THAT WE ARE LOOKING TO SEARCH WILL ALSO BE CAPITAL

# we have found the count of 'I' in 'GAURI GUGLANI'. The for-loop loops over each character of my_string and the if condition checks if each character of my_string is 'I'. The value of count increases if there is a match.

# #METHOD 2- USING COUNT() METHOD

# In[24]:


my_string = "GAURI GUGLANI"
my_char = "I"

print(my_string.count(my_char))


# count() counts the frequency of the character passed as parameter.
