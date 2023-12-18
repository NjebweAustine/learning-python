#!/usr/bin/env python
# coding: utf-8

# INDEXES IN PANDAS

# In[4]:


import pandas as pd


# In[14]:


df=pd.read_csv(r"C:\Users\Augustine\Downloads\world_population.csv")
df


# In[15]:


df.set_index('Country', inplace=True)


# In[16]:


df


# In[8]:


df.reset_index(inplace=True)


# In[9]:


df


# In[39]:


df.set_index(['Continent','Capital'], inplace=True)


# In[24]:


df


# In[26]:


df.sort_index()


# In[32]:


pd.set_option('display.max.rows',235)
df


# In[35]:


df.sort_index(ascending=True)


# In[37]:


df.loc['Africa']


# In[38]:


df.loc['Africa', 'Tunis']


# In[ ]:




