#!/usr/bin/env python
# coding: utf-8

# #Program to Print all Prime Numbers in an Interval

# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6

# In[18]:


# Python program to display all the prime numbers within an interval

#setting up intervals from lowest to highest
lower = 1
upper = 11

print("Prime numbers between", lower, "and", upper, "are:")

#storing in variablr called num
#using for loop in rangebetween lower to upper
#upper+1 will help to include the upper number also
for num in range(lower, upper+1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# #Here, we store the interval as lower for lower interval and upper for upper interval, and find prime numbers in that range.
