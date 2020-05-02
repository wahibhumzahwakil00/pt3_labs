#!/usr/bin/env python
# coding: utf-8

# ### q1 create an empty dictionary

# In[1]:


dict1={}
print(dict1)


# ### q2 with values

# In[2]:


dict1={"A":"amy","B":"bob","C":"carry"}
print(dict1)


# ### q3 for multiple datatype

# In[3]:


dict1={"A":1,"B":"bob","C":"carry"}
print(dict1)


# ### q4 add element

# In[12]:


dict1={"A":1,"B":"bob","C":"carry"}
dict1["X"]=556
print(dict1)


# ### q5 for loop basics

# In[13]:


dict1={"A":1,"B":"bob","C":"carry"}
for key,value in dict1.items():
    print(key,value)
    


# ### q6 print table

# In[22]:


dict2={}
for key in range(1,11):
   dict2[fact]=key*key
print(dict2)
    


# ### q7 factorial

# In[28]:


dict2={}
fact=1
for key in range(1,11):
    dict2[key]=key*key-1)   


# ### q8 check if present or not

# In[30]:


dict1={"A":1,"B":"bob","C":"carry"}
if "A" in dict1:
    print("A is present")
    
    


# ### q9 remove elements from dic

# In[31]:


dict3={1:12,2:23,3:34}
print(dict3)
dict3.clear()
print(dict3)


# ### q10 concatinate the dictionaries

# In[33]:


d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
d3={}
for d in (d1,d2):
    d3.update(d)
print(d3)    


# ### q11 nested dic

# In[34]:


d1={1:"a",2:"b",3:{"c":"carry","d":"john"},4:[1,2,3,4],5:(34,34)}
print(d1)


# ### print element of nested dic

# In[35]:


print(d1[3]["c"])


# ### q12 sum of values in dic

# In[2]:


d3={"a":1,"b":23,"c":30}
sum=0
for i in d3:
    sum=sum+d3[i]
print(sum)    


# In[ ]:




