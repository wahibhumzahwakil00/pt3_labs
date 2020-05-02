#!/usr/bin/env python
# coding: utf-8

# ### ques1

# In[1]:


var1=(2,4,5,)
var1


# ### ques2

# In[2]:


var1=("a",1,"second")
var1


# ### ques3

# In[3]:


var2=(1,2,3,4)
print(var2[1])


# ### ques4

# In[4]:


var2=(1,2,3,4)
a=var2[0]
b=var2[1]
c=var2[2]
d=var2[3]
print(a,b,c,d)
a,b,c,d=var2
print(a,b,c,d)


# ### ques5

# In[5]:


var2=(1,2,3,4)
var2=var2+(9,)
print(var2)
l1=list(var2)
l1.remove(9)
var3=tuple(l1)
print(var3)


# ### ques6

# In[6]:


var1=("a","b","c")
var2=(1,2,3)
str1=" ".join(var1)
print(str1)


# ### ques9

# In[7]:


var1=(1,2,2,2)
print(var1.count(2))


# ### ques10

# In[8]:


var1=(1,2,3,4)
if 2 in var1:
    print("p")
else:
    print("a")


# ### ques 15

# In[9]:


var1=(1,2,3,4)
print(len(var1))


# ### ques14

# In[10]:


var1=(1,2,3,4,5)
print(var1.index(2))


# ### ques7

# In[11]:


var1=(1,2,3,4)
print(var1[0:2]+var1[3:])


# In[ ]:




