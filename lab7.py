#!/usr/bin/env python
# coding: utf-8

# ### q1

# In[1]:


num1=float(input("Enter first number: "))

num2=float(input("Enter second number: "))

mul=num1*num2;

print("the product of given numbers is:",mul)


# ### q2

# In[3]:


num1=float(input("Enter first number: "))

num2=float(input("Enter second number: "))

add=num1+num2;

print("the product of given numbers is:",add)


# ### q3
# 

# In[4]:


def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f)
a=int(input("Enter the number"))    
fact(a)    


# ### q4

# In[5]:


def fib(v):
    a=0
    b=1
    for i in range(v):
        sum=a+b
        print(sum)
        a=b
        b=sum
v=int(input("Enter the limit :"))
fib(v)


# ### q5

# In[7]:


def swap(a,b):
    t=0
    t=a
    a=b
    b=t
    print(a ,b)
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
swap(a,b)


# ### q6

# In[8]:


def hcf(x,y):
    if x<y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            gcd=i
    return gcd
a=int(input("Enter first number"))
b=int(input("Enter second number"))
hcf(a,b)


# ### q7

# In[9]:


x = 0
def ASCII(c):
    x = ord(c)
    return x

c = input("enter a character = ")
print("The ASCII value of '" + c + "' is", ASCII(c))


# ### q8

# In[ ]:


import math
x = 0
def square_root(a):
    x = math.sqrt(a)
    return x

a = int(input("enter an number"))
print("square root of",a,"=",square_root(a))


# ### q9

# In[12]:


import datetime
def dt(x):
    today = datetime.datetime.now()
    return today

print("the current date and time is",dt(x))


# ### q10

# In[14]:


def greet(name,message):
    print("hello",name,".",message)
    
greet("sahiba","how are you?")


# ### q11

# In[16]:


def attendence(name,roll_no,section = "cse-4c"):
    print("details",name + ',' + roll_no + ',' + section)
    
attendence(name = "aliaa",section = "cse-4a",roll_no = "1")
attendence(section ="cse-4b",name = "alisha",roll_no = "2") 
attendence("ahana",roll_no = "7")


# ### q12

# In[17]:


def greeting(name, msg = "how is your day going!"):

   print("Hola",name + ', ' + msg)

greeting("aliaa")
greeting("alia","is everything alright!")


# ### q13

# In[18]:


def my_fun(*argv):  
    for arg in argv:  
        print (arg) 
    
my_fun('Hello', 'hi', 'hola', 'namaste')  


# In[ ]:




