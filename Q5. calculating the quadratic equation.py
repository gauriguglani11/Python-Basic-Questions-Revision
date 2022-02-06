#!/usr/bin/env python
# coding: utf-8

# In[26]:


# program to solve quadratic equation
#steps to solve quadratic eqn
# ax^2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0
# actual solution= (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


# Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

