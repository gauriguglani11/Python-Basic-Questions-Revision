#!/usr/bin/env python
# coding: utf-8

# #Program to Capitalize the First Character of a String

# Two strings are said to be anagram if we can form one string by arranging the characters of another string. For example, Race and Care. Here, we can form Race by arranging the characters of Care.

# In[44]:


my_string = "gauri guglani"

print(my_string[0].upper() + my_string[1:])


# In the above example, my_string[0] selects the first character and upper() converts it to uppercase. Likewise, my_string[1:] selects the remaining characters as they are. Finally they are concatenated using +.

# #using inbuilt method capitalize()

# In[41]:


my_string = "gauri guglani"

cap_string = my_string.capitalize()

print(cap_string)
print(my_string.upper()) #whole string capital


# Note: capitalize() changes the first character to uppercase; however, changes all other characters to lowercase.
