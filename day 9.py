#!/usr/bin/env python
# coding: utf-8

# # Day 9 Assignment 2

# In[42]:


def getAmstrongNumber(num):
    for num in range(1,1000):
        temp=num
        sum=0
        while temp > 0:
            digit= temp%10
            sum=sum+digit**3
            temp=temp//10
            if sum==num:
                print(num)


# In[43]:


print(getAmstrongNumber(num))


# # Day 9 Assignment 1

# In[1]:


import unittest
num=10
if num > 1:
    for i in range(2,num):
        if (num % i)==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

