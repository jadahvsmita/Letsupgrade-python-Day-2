#!/usr/bin/env python
# coding: utf-8

# # List and its default functions

# In[1]:


lst=[10,15,20,25,30,35,40]
lst


# In[2]:


lst[1]


# In[3]:


lst.append(45)
lst


# In[4]:


lst.insert(2,15.5)
lst


# In[5]:


lst.count(15)


# In[6]:


lst.pop(2)


# In[7]:


lst.index(15)


# In[8]:


lst1=[1,2,3,4]


# In[9]:


lst.extend(lst1)
lst


# In[10]:


lst.copy()


# In[11]:


lst.reverse()
lst


# In[12]:


lst.remove(4)
lst


# In[13]:


lst.clear()
lst


# # 2. Dictionary and its default functions

# In[14]:


dct={'Name':'Smita','Age':22,'Education':'Msc-Statistics'}
dct


# In[15]:


dct.copy()
dct


# In[16]:


dct.get('Name')


# In[17]:


dct.items()
dct


# In[18]:


dct.keys()
dct


# In[19]:


dct.pop('Age')
dct


# In[21]:


dct.popitem()
dct


# In[22]:


dct1={'number':2345}


# In[23]:


dct.update(dct1)
dct


# In[24]:


dct.clear()
dct


# # Sets and its default functions

# In[3]:


s={1,2,3,4,5}     # set
s


# In[4]:


s.add(6)
s


# In[5]:


s.copy()
s


# In[6]:


s1={3,4,5,6,7}
s1


# In[7]:


s.union(s1)
s


# In[8]:


s.intersection(s1)
s


# In[9]:


s1.issubset(s)


# In[10]:


s1.isdisjoint(s)


# In[11]:


s.clear()
s


# # 4.Tuple and explore default methods

# In[12]:


tuple=(1,6,3.8,6)
tuple


# In[13]:


tuple.count(6)


# In[14]:


tuple.index(1)


# In[15]:


type(tuple)


# In[16]:


max(tuple)


# In[17]:


min(tuple)


# # 5. string and explore default methods

# In[18]:


string="Python Essentials Program"
string


# In[19]:


type(string)


# In[20]:


string[0]


# In[21]:


string[6:16]


# In[22]:


string1="With Letsupgrade"


# In[23]:


print( string+ string1)

