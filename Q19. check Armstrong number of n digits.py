#!/usr/bin/env python
# coding: utf-8

# #Program to Check Armstrong Number

# In[27]:


#check Armstrong number of n digits
num = 1634

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# 

# In[26]:


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# Here, we ask the user for a number and check if it is an Armstrong number.
# 
# We need to calculate the sum of the cube of each digit. So, we initialize the sum to 0 and obtain each digit number by using the modulus operator %. The remainder of a number when it is divided by 10 is the last digit of that number. We take the cubes using exponent operator.
# 
# Finally, we compare the sum with the original number and conclude that it is Armstrong number if they are equal.
