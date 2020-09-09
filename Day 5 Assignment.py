#!/usr/bin/env python
# coding: utf-8

# # Make a function for prime numbers and use filter to filter out all theprime numbers from 1-2500 (Assignmet 2- Day 5)

# In[25]:


def is_prime(number):
     for i in range (2,number):
        if number % i == 0:
             return False
        else:    
             return True


# In[27]:


fltr=filter(is_prime,range(2500))
print('prime numbers between 1-2500:', list(fltr))


# # Program to identify sublist [1,1,5] 

# In[1]:


#initializing the list
test_list =[1,5,6,4,1,2,3,5]
sub_list=[1,1,5]
print("original list :" + str(test_list))
print("Original sub list:" +str(sub_list))
flag=0
if(set(sub_list).issubset(set(test_list))):
    flag=1
    if(flag):
        print("Yes, its a match")
    else:
        print("No, its Gone")


# In[2]:


#initializing the list
test_list =[1,5,6,5,1,2,3,6]
sub_list=[1,1,5]
print("original list :" + str(test_list))
print("Original sub list:" +str(sub_list))
flag=0
if(set(sub_list).issubset(set(test_list))):
    flag=1
    if(flag):
        print("Yes, its a match")
    else:
        print("No, its Gone")


# # Lambda function for capitalizing the whole sentence passed using arguments 

# In[5]:


list1=['hey!', 'i am smita']
list2=list(map(lambda x:x.title(),list1))
print(list2)

