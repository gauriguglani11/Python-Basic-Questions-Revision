#!/usr/bin/env python
# coding: utf-8

# #Program to Compute the Power of a Number

# In[5]:


base = 3
exponent = 2

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))


# In this program, base and exponent are assigned values 3 and 4 respectively.
# 
# Using the while loop, we keep on multiplying the result by base until the exponent becomes zero.
# 
# In this case, we multiply result by base 4 times in total, so result = 1 * 3 * 3 * 3 * 3 = 81

# Example 2: Calculate power of a number using a for loop

# In[6]:


base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))


# Here, instead of using a while loop, we've used a for loop.
# 
# After each iteration, the exponent is decremented by 1, and the result is multiplied by the base exponent number of times.
# 
# Both programs above do not work if you have a negative exponent. For that, you need to use the pow() function in the Python library.

# Example 3: Calculate the power of a number using pow() function

# In[9]:


base = -3
exponent = -4

result = pow(base, exponent)

print("answer = " + str(result))


# pow() accepts two arguments: base and exponent. In the above example, -3 raised to the power -4 is calculated using pow()
