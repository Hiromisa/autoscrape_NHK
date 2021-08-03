#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url ='https://www3.nhk.or.jp/news/catnew.html?utm_int=all_header_menu_news-new'
response = requests.get(url)
response.encoding = response.apparent_encoding
doc = BeautifulSoup(response.text, 'html.parser')




# In[7]:


# stories = doc.select('dl')
# for story in stories:
#     print('------')
#     print(story.select_one('.title').text.strip())
#     print('https://www3.nhk.or.jp/' + story.select_one('a')['href'])
#     print(story.select_one('time').text.strip())
#     try:
#         print(story.select_one('.i-word').text.strip())
#     except:
#         print('no category')


# In[8]:


stories = doc.select('dl')
list = []
for story in stories:
    dict = {}
    dict['title'] = story.select_one('.title').text.strip()
    dict['link'] = 'https://www3.nhk.or.jp/' + story.select_one('a')['href']
    dict['time'] = story.select_one('time').text.strip()
    try:
        dict['category'] = story.select_one('.i-word').text.strip()
    except:
        print('no category') 
#     print(dict)
    list.append(dict)


# In[9]:


list


# In[10]:


df = pd.DataFrame(list)
df


# In[11]:


df.to_csv('nhk-latest20news.csv',index=False)


