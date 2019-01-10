#!/usr/bin/env python
# coding: utf-8
主要是损失函数
# In[14]:


import numpy as np
import matplotlib.pyplot as plt

1、平方差损失函数
注重的是错误分类和正确的分类，当有异常点出现的时候会对异常点敏感
# In[9]:


y = np.array([1, 2,3 ])
t = np.array([1, 3, 2])


# In[10]:


def mse(y, t):
    return np.sum((y - t)**2)


# In[11]:


mse(y, t)


# In[72]:


#画图
import matplotlib
fig = plt.figure()
real = np.repeat(100, 1000)   #100重复1000次
pre = np.arange(-1000, 1000, 2)
loss_result = [mse(real[i], pre[i]) for i in range(len(pre))]

plt.plot(pre, loss_result)
plt.savefig('D:/1.jpg')

2、平均绝对损失函数MAE
不会放大异常点
但是他的梯度更新总是相同的，可增加一个变化的学习率
# In[20]:


def mae(y, t):
    return np.sum(np.abs(y - t))


# In[73]:


#画图
fig = plt.figure()
loss_result = [mae(real[i], pre[i]) for i in range(len(pre))]
plt.plot(pre, loss_result)
plt.savefig('D:/2.jpg')

3、Huber loss平滑平均绝对误差
克服了mae和mse的缺点，对异常值不敏感，并保持连续可导
但是当损失很大的时候，接近于常数
# In[66]:


def huber(y, t, sig):
    loss = np.where(np.abs(y-t)<sig, 0.5*((y-t)**2), sig*np.abs(y-t)-0.5*(sig**2))    
    return np.sum(loss)


# In[74]:


fig, ax = plt.subplots(1,1, figsize=(7,5))
real = np.repeat(0, 1000) 
pre = np.arange(-10,10, 0.02)
sig = [0.1, 1, 10]
loss_result = [[huber(real[i], pre[i], q) for i in range(len(pre))] for q in sig]
for i in range(len(sig)):
    ax.plot(pre, loss_result[i], label=sig[i])
ax.legend()
ax.set_ylim(bottom=-1, top=15)
fig.tight_layout()
plt.savefig('D:/3.jpg')

4、log cosh
比L2更加平滑
# In[49]:


def log_cosh(y, t):
    loss = np.log(np.cosh(y - t))
    return np.sum(loss)


# In[75]:


fig = plt.figure()
real = np.repeat(0, 1000) 
pre = np.arange(-10,10, 0.02)
loss_result = [log_cosh(real[i], pre[i]) for i in range(len(real))]
plt.plot(pre, loss_result)
plt.show()
plt.savefig('D:/4.jpg')

5、entropy交叉熵损失函数
注重预测分类正确的结果
# In[61]:


def entropy(p):
    loss = -1*p*np.log(p)
    return np.sum(loss)


# In[65]:


p = np.arange(0.1, 0.6, 200)
loss_result = [entropy(p[i]) for i in range(len(p))]
loss_result

