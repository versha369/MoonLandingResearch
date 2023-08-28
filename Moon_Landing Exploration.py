#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np


# In[29]:


dk = pd.read_csv('Moonlanding.csv',encoding='latin-1')


# In[30]:


dk.head()


# In[31]:


dk.info()


# In[32]:


dk.describe().T


# In[33]:


dk.describe().T.style.background_gradient()


# In[36]:


dk.shape


# In[37]:


df.dtypes


# In[38]:


df.dropna(inplace=True)


# In[39]:


df.shape


# In[40]:


df.isnull().sum()


# In[41]:


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotblib', 'inline')
sns.set_style('darkgrid')


# In[42]:


df.columns


# In[44]:


df['Mission'].value_counts()


# In[46]:


df[df['Mission'] == "Chang'e 5"]


# In[47]:


df['Mission Type'].value_counts()


# In[49]:


plt.figure(figsize=(20,10))
sns.countplot(data=df,x=df['Mission Type'], palette='rocket')
plt.xlabel('Mission Type')
plt.xticks(rotation=90)
plt.show()


# In[51]:


pd.DataFrame(df.groupby(['Operator']).count()['Mission'].sort_values(ascending=False))


# In[52]:


label = df['Operator'].unique()


# In[53]:


plt.pie(df['Operator'].value_counts(10), labels=label, shadow=True)
plt.show()


# In[54]:


df['Outcome'].value_counts()


# In[57]:


plt.figure(figsize=(10,5))
sns.countplot(data=df,x = df['Outcome'],palette='coolwarm')
plt.xticks(rotation=90)
plt.xlabel('Result of an operation')
plt.show()


# In[58]:


df.head()


# In[59]:


plt.figure(figsize=(15,12))
df['Carrier Rocket'].value_counts().sort_values(ascending=True).plot(kind='barh')
plt.show()


# In[60]:


df['Launch Date'] = df['Launch Date'].str.replace('-','/')


# In[61]:


df.head()


# In[62]:


df[df['Operator']== 'India ISRO']


# In[ ]:




