#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd


# In[58]:


nari_static = pd.read_csv(r'C:\Users\user\Desktop\MongoData\AisData\nari_static.csv', low_memory=False)
ship_types = pd.read_csv(r'C:\Users\user\Desktop\MongoData\AisTypes\Ship_Types_List.csv', low_memory=False)
nari_dynamic = pd.read_csv(r'C:\Users\user\Desktop\MongoData\AisData\nari_dynamic.csv', low_memory=False)


# In[59]:


nari_static.shape


# In[60]:


nari_dynamic.shape


# In[61]:


nari_static = nari_static[:100000]


# In[62]:


nari_dynamic = nari_dynamic[:100000]


# In[63]:


nari_static.shape


# In[64]:


nari_dynamic.shape


# In[65]:


ship_types.head()


# In[66]:


nari_static.head()


# In[80]:


nari_dynamic.head()


# In[69]:


total = nari_static.isnull().sum().sort_values(ascending=False)
percent = (nari_static.isnull().sum()/nari_static.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#missing_data.head(20)


# In[68]:


nari_static.drop(['mothershipmmsi'],axis=1,inplace=True)


# In[70]:


total = nari_dynamic.isnull().sum().sort_values(ascending=False)
percent = (nari_dynamic.isnull().sum()/nari_dynamic.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#missing_data.head(20)


# In[71]:


nari_static.fillna(nari_static.mean())


# In[73]:


nari_static.to_csv('nari_static_new.csv')


# In[74]:


nari_dynamic.to_csv('nari_dynamic_new.csv')


# In[ ]:




