#!/usr/bin/env python
# coding: utf-8

# ### ques1

# In[5]:


total = 0
l =[1,2,3,4,5]
for x  in range(0, len(l)):
       total = total + l[x]

print("Sum of all elements in given list: ", total)


# ### ques2

# In[6]:


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))


# ### ques3

# In[7]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# ### ques4

# In[8]:


def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))


# ### ques5

# In[12]:


def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
              ctr += 1
    return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# ### ques6

# In[14]:


def last(n): return n[-1]

def sort_list_last(tuples):
       return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])) 


# ### ques7

# In[16]:


a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# ### ques8

# In[17]:


l = []
if not l:
      print("List is empty")


# ### ques9

# In[18]:


original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


# ### ques10

# In[19]:


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# ### ques11

# In[22]:


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


# ### ques12

# In[23]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# In[ ]:




