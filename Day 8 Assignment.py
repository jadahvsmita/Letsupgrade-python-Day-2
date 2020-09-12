#!/usr/bin/env python
# coding: utf-8

# # Day 8 Assignment 1

# In[43]:


fibonacci_cache={}
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n==1:
        value=1
    elif n==2:
         value=1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_cache[n]=value
    return value
for n in range(1, 10):
     print(n, fibonacci(n))
    


# # Assignment 2 Day 8

# In[26]:


try:
    fob=open("test","r")
    fob.write("It's my test file to verify exception handling in python!")
except IOError:
    print("Error: can\'t find the file or read data")
else:
    print("Write operation is performed siccessfully on the file")

