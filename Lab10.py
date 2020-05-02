#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1
class Animal:
    def legs(self):
        print("animals have 4 legs")
class Tiger(Animal):
    pass
class Dog(Animal):
    Animal().legs()
Tiger().legs()


# In[2]:


#Q.2
class Employee:
    def printDesignation():
        pass
class Engineer(Employee):
    def printDesignation():
        print("Engineer")
class Manager(Employee):
    def printDesignation():
        print("Manager")
Engineer.printDesignation()
Manager.printDesignation()


# In[3]:


#Q.3
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calc(self):
        self.a+self.b


# In[4]:


#Q.4
class P:
    def __init__(self):
        self.p="Parent class"
    def show(self):
        print(self.p)
class C(P):
    def __init__(self):
        self.p="Child class"
    def sho(self):
        print(self.p)
new=P()
new1=C()
new.show()
new1.show()


# In[5]:


#Q.5
class A:
    def m(self):
        print("A")
class B:
    def n(self):
        print("B")
class C(A,B):
    def o(self):
        print("C")
x=C()
x.m()
x.n()
x.o()


# In[ ]:




