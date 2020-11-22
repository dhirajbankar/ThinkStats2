#!/usr/bin/env python
# coding: utf-8

# # Examples and Exercises from Think Stats, 2nd Edition
# 
# http://thinkstats2.com
# 
# Copyright 2016 Allen B. Downey
# 
# MIT License: https://opensource.org/licenses/MIT
# 

# In[8]:


preg.birthord.isnull().sum()


# In[9]:


from __future__ import print_function, division

import nsfg


# ## Examples from Chapter 1
# 
# Read NSFG data into a Pandas DataFrame.

# In[10]:


preg = nsfg.ReadFemPreg()
preg.head()


# Print the column names.

# In[11]:


preg.columns


# Select a single column name.

# In[12]:


preg.columns[1]


# Select a column and check what type it is.

# In[13]:


pregordr = preg['pregordr']
type(pregordr)


# Print a column.

# In[14]:


pregordr


# Select a single element from a column.

# In[15]:


pregordr[0]


# Select a slice from a column.

# In[16]:


pregordr[2:5]


# Select a column using dot notation.

# In[17]:


pregordr = preg.pregordr


# Count the number of times each value occurs.

# In[18]:


preg.outcome.value_counts().sort_index()


# Check the values of another variable.

# In[19]:


preg.birthwgt_lb.value_counts().sort_index()


# Make a dictionary that maps from each respondent's `caseid` to a list of indices into the pregnancy `DataFrame`.  Use it to select the pregnancy outcomes for a single respondent.

# In[20]:


caseid = 10229
preg_map = nsfg.MakePregMap(preg)
indices = preg_map[caseid]
preg.outcome[indices].values


# ## Exercises

# Select the `birthord` column, print the value counts, and compare to results published in the [codebook](http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611933)

# In[21]:



pregordr = preg['birthord']
pregordr
type(pregordr)


# We can also use `isnull` to count the number of nans.

# Select the `prglngth` column, print the value counts, and compare to results published in the [codebook](http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611931)

# In[24]:


prglngth = preg['prglngth'].value_counts()
prglngth


# To compute the mean of a column, you can invoke the `mean` method on a Series.  For example, here is the mean birthweight in pounds:

# In[16]:


preg.totalwgt_lb.mean()


# Create a new column named <tt>totalwgt_kg</tt> that contains birth weight in kilograms.  Compute its mean.  Remember that when you create a new column, you have to use dictionary syntax, not dot notation.

# In[25]:


preg['totalwgt_kg'] = preg['basewgt']


# `nsfg.py` also provides `ReadFemResp`, which reads the female respondents file and returns a `DataFrame`:

# In[26]:


resp = nsfg.ReadFemResp()


# `DataFrame` provides a method `head` that displays the first five rows:

# In[27]:


resp.head()


# Select the `age_r` column from `resp` and print the value counts.  How old are the youngest and oldest respondents?

# In[31]:


# Solution goes here
resp.columns[7]


# We can use the `caseid` to match up rows from `resp` and `preg`.  For example, we can select the row from `resp` for `caseid` 2298 like this:

# In[21]:


resp[resp.caseid==2298]


# And we can get the corresponding rows from `preg` like this:

# In[22]:


preg[preg.caseid==2298]


# How old is the respondent with `caseid` 1?

# In[34]:


# Solution goes here
resp[resp.caseid==2298]['age_r']


# What are the pregnancy lengths for the respondent with `caseid` 2298?

# In[35]:


# Solution goes here
resp[resp.caseid==2298]


# What was the birthweight of the first baby born to the respondent with `caseid` 5012?

# In[36]:


# Solution goes here
resp[resp.caseid==5012]['basewgt']


# In[ ]:




