#!/usr/bin/env python
# coding: utf-8

# ### ques1

# In[1]:


counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


# ### ques5

# In[8]:


a=input("enter a string\n")
len(a) 


# ### ques6

# In[10]:


a=input("enter a string\n")
count=0
for char in a:
    count+=1
    print(count)


# ### ques7

# In[11]:


A=input("ENTER A STRING\n")
if len(A)>2:
    f=A[0:2]+A[-2:]
    print(f)
else:
    print(A)


# ### ques8

# In[12]:


s=input("enter a string\n")
char1=s[0:1]
s1=s.replace(char1,'$')
char1+s1[1:]


# ### ques9

# In[13]:


r=input("enter the 1st string\n")
s=input("enter the 2nd string\n")
char1=r[0:1]
r=r.replace(r[0:1],s[0:1])
s=s.replace(s[0:1],char1)
print(r,s)


# ### ques10

# In[ ]:


r=input("enter a string\n")
if len(r)>3:
    s=r+"ing"
    print(s)
if  r[-3:]=="ing":
    r=r.replace(r[-3:],"ly")
else:
    print(r)

