#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
from urllib.request import urlopen
import numpy as np
import urllib.request, urllib.parse, urllib.error


# In[43]:


w_list=[]
fh = urllib.request.urlopen('https://www.gutenberg.org/files/2600/2600-0.txt')
for line in fh:
    ldata= line.decode().strip()
    #spliting the words and removing the special characters 
    words = ldata.split()
    words = [word.strip('.,!;\\()"$#/[]:*-?') for word in words]
    words= [x.lower() for x in words]
    [w_list.append(word) for word in words]


# In[44]:


# converting list of words into array    
word_array = np.array(w_list)
unique_words=np.unique(word_array)
print(' Number of unique words in Tolstoy’s War and Peace: ',len(unique_words))


# In[ ]:





# In[ ]:





# In[ ]:




