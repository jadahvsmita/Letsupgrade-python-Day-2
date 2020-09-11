#!/usr/bin/env python
# coding: utf-8

# # Day 6 Assignments letsupgrade

# In[ ]:


class Account(object):
    def __init__(self, ownerName, Balance):
        self.ownerName=ownerName
        self.Balance=Balance
    def __str__(self):
        return 'Account ownerName: 
            {owner}\nAccount Balance:
            ${balance}'.format(ownerName=self.ownerName,balance=self.Balance)
    def deposit(self, dp_money):
        self.balance+= dp_money
        print('Deposit accepted your balance is-')
        Balance = self.Balance
    def withdraw(self, wd_money):
        if wd_money > self.Balance:
             print('Funds unavailable!')
        else:
            self.Balance-=wd_money
            print('withdawal acceptes your balance is-')
            Balance=self.Balance
acct1=Account('Smita',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)


# In[13]:


import math
class cone():
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def volume(self):
        return math.pi*(self.radius**2)
    def area(self):
        return math.pi*(self.radius)*(self.height)+math.pi*(self.radius)**2
r=int(input("Enter radius of cone:"))
h=int(input("Enter height of cone:"))
obj=cone(r,h)
print("Volume of cone:",obj.volume())
print("surface area of cone :",obj.area())

