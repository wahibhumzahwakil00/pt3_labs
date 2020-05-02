#!/usr/bin/env python
# coding: utf-8

# ### ques1
# 
# 

# In[1]:


num=int(input("enter a no\n"))
if num%2==0:
    print("even number")
else:
    print("odd no")


# ### ques2
# 

# In[2]:


num=int(input("enter a number\n"))
if num%4==0:
    print("year is leap year")
else:
    print("year is not leap year")


# ### ques3

# In[3]:


num=input("enter a character")
if num=='a'or num=='e'or num=='i'or num=='o'or num=='u'or num=='A'or num=='E'or num=='I'or num=='O'or num=='U':
    print("character is a vowel")
else:
    print("character is consonent")


# 
# ### ques4

# In[4]:


num1=int(input("enter first no"))
num2=int(input("enter the second no"))
if num1>num2:
    print("smaller no",num2)
else:
    print("smaller no",num1)


# ### ques5

# In[5]:


num=int(input("enter a no"))
factorial=1
if num<0:
    print("invalid no")
if num==0:
    print("factorial is 1")
else:
    for i in range(1,num +1):
        factorial=factorial*i
    print("factorial of  is", factorial)


# ### ques6

# In[6]:


for i in range(0,4):
    for s in range(0,4-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()    


# ### ques7

# In[19]:


num1=0
num2=1
sum=0
while sum<=13:
    print(sum)
    num1=num2
    num2=sum
    sum=num1+num2


# ### ques8

# In[27]:


num=int(input("enter a no"))
for i in range(1,num):
    if(num%i==0):
        print(num,"is not prime")
        break
        
else:
    print(num,"is prime")


# ### ques9

# In[29]:


print("1 for sum")
print("2 for subtract")
print("3 for divide")
print("4 for multiply")
num1=int(input("enter the first no"))
num2=int(input("enter the second no"))
num3=int(input("enter the choice"))
if num3==1:
    sum=num1+num2
    print(sum)
if num3==2:
    sub=num1-num2
    print(sub)
if num3==3:
    div=num1/num2
    print(div)
if num3==4:
    mul=num1*num2
    print(mul)
else:
    print("enter correct operation")
    


# In[ ]:




