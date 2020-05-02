#!/usr/bin/env python
# coding: utf-8

# ### q1

# In[2]:


class Triangle:
    def _init_(self):
            self.a=0
            self.b=0
            self.c=0
    def create_triangle(self):
        self.a=int(input("enter the first side"))
        self.b=int(input("enter the second side"))
        self.c=int(input("enter the third side"))
    def print_sides(self):
        print("first side:",self.a,"second side:",self.b,"third side",self.c)
x=Triangle()
x.create_triangle()
x.print_sides()


# ### q2

# In[4]:


class String():
    def _init_(self):
        self.str1=""
    def inputstr(self):
        self.str1=input("enter the string")
    def printstr(self):
        print(self.str1)
x=String()
x.inputstr()
x.printstr()


# ### q3

# In[4]:


class Rectangle:
    length=0.0
    width=0.0
    per=0.0
    def rect_values(self,l,w):
        self.length=l
        self.width=w
    def perimeter(self):
        self.per=2*self.length+self.width
        return(self.per)    
r1=Rectangle()
r1.rect_values(10,20)
k=r1.perimeter()
print("the perimeter of rectangle is",k)


# ### q4

# In[6]:


class Circle:
    radius=0.0
    area=0.0
    peri=0.0
    def _init_(self,radius):
        self.radius=radius
    def area(self):
        self.area=3.14*self.radius*self.radius
        return(self.area)
    def perimeter(self):
        self.peri=2*3.14*self.radius
        return(self.peri)
c1=Circle()
c1._init_(4)
a=c1.area()
p=c1.perimeter()
print("the area and perimeter of circle are:",a,p)
        


# ### q5

# In[7]:


class Class2:
    pass
class Class3:
    def m(self):
        print("in class3")
class Class4(Class2,Class3):
    pass
obj=Class4()
obj.m()


# In[ ]:




