#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd


# In[3]:


a = {"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}


# In[8]:


b = pd.DataFrame(a)

取列
# In[12]:


#返回<class 'pandas.core.series.Series'>
print(b.a)
print(type(b.a))


# In[13]:


#返回<class 'pandas.core.series.Series'>
print(b["b"])
print(type(b["b"]))


# In[14]:


#返回<class 'pandas.core.frame.DataFrame'>
print(b[["b"]])
print(type(b[["b"]]))


# In[19]:


print(b[["a":"b"]])

取行
# In[17]:


#前闭后开
b[0:2]  


# iloc可以同时取行和列

# In[27]:


#<class 'pandas.core.series.Series'>
print(b.iloc[0])
print(type(b.iloc[0]))


# In[28]:


b.iloc[0:2]


# In[29]:


b.iloc[:,1]


# In[31]:


#<class 'numpy.ndarray'>
print(b.values)
print(type(b.values))


# ix取某一行（不建议使用）

# In[32]:


b.ix[0]

loc和iloc的区别
# In[33]:


#左右都闭
b.loc[0:2]


# In[34]:


#左开右闭
b.iloc[0:2]


# In[42]:


#切片，列部分不用加[]
b.iloc[:,0:3]


# In[50]:


#error行标签已经定义了，无法用loc数字切片
#b.loc[:,[0:3]]


# In[51]:


#错误方法
#b.iloc[:,"a":"c"]
#正确写法
b.iloc[:,0:3]


# In[53]:


#loc切片不用加[]
b.loc[:,"a":"c"]


# In[54]:


#loc选多个标签需要加[]
b.loc[:,["a","b"]]

