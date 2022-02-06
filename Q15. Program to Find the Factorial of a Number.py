#!/usr/bin/env python
# coding: utf-8

# #Program to Find the Factorial of a Number

# In[19]:


#printing factorial of the number

#taking input from user
num = int(input("enter the number to get factorial"))

#defining the 1st value of factorial
fact = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial of",num,"is",fact)


# #Here, the number whose factorial is to be found is stored in num, and we check if the number is negative, zero or positive using if...elif...else statement. If the number is positive, we use for loop and range() function to calculate the factorial.

# #Factorial of a Number using Recursion

# In[21]:


# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 5

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


# #In the above example, factorial() is a recursive function that calls itself. Here, the function will recursively call itself by decreasing the value of the x.
