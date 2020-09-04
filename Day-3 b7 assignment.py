#!/usr/bin/env python
# coding: utf-8

# # Assignment -1

# In[4]:


Input=1000
if Input <=1000 :
    print("Tell the piolt to land the plane")
elif (Input > 1000) and (Input < 5000):
    print("Tell the pilot to come down to 1000ft")
else:
    print("Tell the pilot to come to ground and try later" )
    
    


# In[7]:


Input=4500
if Input <=1000 :
    print("Tell the piolt to land the plane")
elif (Input > 1000) and (Input < 5000):
    print("Tell the pilot to come down to 1000ft")
else:
    print("Tell the pilot to come to ground and try later" )
    


# In[8]:


Input=6500
if Input <=1000 :
    print("Tell the piolt to land the plane")
elif (Input > 1000) and (Input < 5000):
    print("Tell the pilot to come down to 1000ft")
else:
    print("Tell the pilot to come to ground and try later" )
    


# # Assignment 2

# In[9]:


#Printing all the prime numbers between 1-200
for i in range(1,200):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

