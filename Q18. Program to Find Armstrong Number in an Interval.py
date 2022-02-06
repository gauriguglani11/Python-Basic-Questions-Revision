#!/usr/bin/env python
# coding: utf-8

# #Program to Find Armstrong Number in an Interval

# abcd... = a^n + b^n + c^n + d^n + ...

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

# In[24]:


# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

    #storing num in temp variable
   temp = num
   while temp > 0:
       digit = temp % 10
       sum = sum+ digit ** order
       temp //= 10

   if num == sum:
       print(num)


# Here, we have set the lower limit 100 in variable lower and upper limit 2000 in variable upper. We have used for loop to iterate from variable lower to upper. In iteration, the value of lower is increased by 1 and checked whether it is an Armstrong number or not.
# 
# You can change the range and test out by changing the variables lower and upper. Note, the variable lower should be lower than upper for this program to work properly.
