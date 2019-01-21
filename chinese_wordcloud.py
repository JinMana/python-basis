#!/usr/bin/env python
# coding: utf-8

# In[3]:


import jieba
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np


# In[48]:


text2 = open("wordcloud.txt",'r').read()
cut_text = " ".join(jieba.cut(text2))
color_mask= imread("pig.jpg")
#显示的是中文，要用字体包,去掉停用词
#增加停用词
STOPWORDS.add("一个")
cloud = WordCloud(font_path = "./fonts/simhei.ttf", background_color="white", mask=color_mask, max_words=2000, max_font_size=40,stopwords=STOPWORDS)
my_cloud2 = cloud.generate(cut_text)
plt.axis("off")
plt.imshow(my_cloud2)
plt.show()

