#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
import urllib.request
import pandas as pd
import re
import string


# In[7]:


#passing the URL for the book:
downloadURL = "https://www.gutenberg.org/files/2600/2600-0.txt"

#creating a request object:
req = requests.get(downloadURL)


# In[8]:


#let's see the information about the file using .headers method:
req.headers

#checking out the file name: 
file_name = req.url[downloadURL.rfind('/')+1:]

print(file_name)


# The name of the original file is "2600-0.txt"

# In[11]:


#Let's start downloading the file
#I have renamed this as 'peace_war'
open('peace_war','wb').write(req.content) #downloads a file local


# In[12]:


filename = 'peace_war' 
file = open(filename,'r',encoding= 'utf8')
text = file.read().lower() #making all alphabets into lower case
file.close()

#checking the type of text
#print(type(text))
#print(text[:2000])

#checking the output of .lower() method on text:
#print(text[:2000])


# In[13]:


#using dot split method to split the string from white space:
words = text.split() 
print(type(words)) #checking the type of words
#print(words[:200])


# In[16]:


#removing the punctuation from the list of string using string.punctuation method:
table = str.maketrans("","",string.punctuation)
words = [w.translate(table) for w in words]
#print(words[:2000])


# In[17]:


#replacing any character with empty spaces using regex.sub() method:
words= [re.sub(r'\W+','',word) for word in words]
#print(words[:2000])


# In[18]:


#removing any digit like string in our list using isdigit() method:
words = [i for i in words if not i.isdigit()]
#print(words[:2000])


# In[19]:


#using set method to count only the unique words in the list:

unique_words = set(words)   #setting == words [ list we just cleaned]
unique_word_count = len(unique_words) 
print(unique_word_count)


# In[ ]:




