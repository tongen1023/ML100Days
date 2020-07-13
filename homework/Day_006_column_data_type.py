#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd


# In[2]:


app_train = pd.read_csv(r'Desktop\application_train.csv')


# In[3]:


sub_train = pd.DataFrame(app_train['WEEKDAY_APPR_PROCESS_START'])
print(sub_train.shape)
sub_train.head()


# In[4]:


sub_train = pd.get_dummies(sub_train['WEEKDAY_APPR_PROCESS_START'])
print(sub_train.shape)
sub_train.head()


# In[ ]:




