#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


book = requests.get('https://www.gutenberg.org/files/2600/2600-0.txt')


# In[3]:


type(book)


# In[4]:


book.status_code


# In[5]:


book.text[:100]


# In[6]:


len(book.text)


# In[7]:


book_text = book.text.replace('.', '')


# In[8]:


book_text = book_text.lower()


# In[10]:


book_text[:1000]


# In[11]:


book_text = book_text.replace('\r\n', ' ')


# In[12]:


book_text[:1000]


# In[13]:


list_of_words = book_text.split(' ')


# In[14]:


len(list_of_words)


# In[15]:


list_of_words[:100]


# In[16]:


deduped_words = set(list_of_words)


# In[17]:


len(deduped_words)


# In[18]:


from collections import Counter


# In[19]:


counter = Counter(list_of_words)


# In[20]:


len(counter)


# In[22]:


counter.get('tolstoy')


# In[23]:


deduped_list = list(deduped_words)


# In[24]:


type(deduped_words), type(deduped_list)


# In[25]:


print(f"there are {len(deduped_list)} words in War and Peace")


# In[ ]:




