#!/usr/bin/env python
# coding: utf-8

# ### ques1

# In[1]:


class Triangle:
    a=0
    b=0
    c=0
    def create_triangle(self):
        self.a=int(input("Enter The First Side: "))
        self.b=int(input("Enter The Second Side:  "))
        self.c = int(input("Enter The Third Side:  "))
    def printside(self):
        print(self.a)
        print(self.b)
        print(self.c)

tr=Triangle()
tr.create_triangle()
print("The Sides Of Triangle are")
tr.printside()


# ### ques2

# In[2]:


class String:
    a=""
    def gets(self):
        self.a=input("Enter The String:  ")
        return (self.a)
str=String()
print("The input string is: " ,str.gets())


# ### ques3

# In[3]:


class Rectangle:
    l=0.0
    w=0.0
    def rect(self):
        self.l=int(input("Enter The length: "))
        self.w=int(input("Enter The width: "))
        return (2*(self.l+self.w))
r1=Rectangle()
print("The Perimeter of Rectangle is: ",r1.rect())


# ### ques4

# In[4]:


class Circle:
    rad=0.0
    def __init__(self):
        self.rad=float(input("Enter The Radius: "))
    def areac(self):
        return (3.14*self.rad*self.rad)
    def perr(self):
        return (2*3.14*self.rad)
c1=Circle()
print("The Area Of the circle is: " ,c1.areac())
print("The Perimeter of the rectangle is: " , c1.perr())


# ### ques5

# In[ ]:




