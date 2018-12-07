#!/usr/bin/env python
# coding: utf-8
处理json数据
并且将文件名重写
# In[2]:


import json


# In[3]:


file = open("AgriculturalDisease_trainingset\AgriculturalDisease_train_annotations.json")


# In[4]:


#加载json文件
data = json.load(file)


# In[5]:


#list
type(data)


# In[6]:


#dict
type(data[0])


# In[7]:


#int
type(data[0]['disease_class'])


# In[8]:


#str
type(data[0]["image_id"])


# In[9]:


#'1_62fd8bf4d53a1b94fbac16738406f10b.jpg'
str(data[0]['disease_class'])+"_"+data[0]["image_id"]


# In[11]:


#文件夹下的文件列表
import os


# In[12]:


old_name = os.listdir(path = "AgriculturalDisease_trainingset\images")


# In[18]:


#注意rename的时候要写上总的路径，不然会出错
path = "AgriculturalDisease_trainingset\images"
for i in range(len(data)):
    new_name = str(data[i]["disease_class"])+"_"+data[i]["image_id"]
    new_name = os.path.join(path, new_name)
    old_name[i] = os.path.join(path, old_name[i])
    os.rename(old_name[i], new_name)
    print(new_name)

