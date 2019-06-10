#!/usr/bin/env python
# coding: utf-8

# **EXPLORE HACKER NEWS POSTS**

# In this project, we'll work with a data set of submissions to popular technology site Hacker News.
# 
# We're specifically interested in posts whose titles begin with either Ask HN or Show HN. Users submit Ask HN posts to ask the Hacker News community a specific question.Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.
# 
# We'll compare these two types of posts to determine the following:
# 
# **Do Ask HN or Show HN receive more comments on average?
# Do posts created at a certain time receive more comments on average?**

# #IMPORT DATA

# In[2]:


from csv import reader
opened_file = open("hacker_news.csv")
read_file = reader(opened_file)
hn = list(read_file)
headers = hn[0]
hn = hn[1:]
print(headers)


# In[3]:


print(hn[:5])


# In[4]:


ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1]
    title = title.lower()
    if title.startswith("ask hn"):
        ask_posts.append(post)
    elif title.startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[5]:


print(ask_posts[:5])
print(show_posts[:5])


# In[6]:


total_ask_comments = 0
for ask in ask_posts:
    num_comments = ask[4]
    num_comments = int(num_comments)
    total_ask_comments += num_comments

avg_ask_comments = total_ask_comments/len(ask_posts)
print(avg_ask_comments)

total_show_comments = 0
for show in show_posts:
    num_comments = show[4]
    num_comments = int(num_comments)
    total_show_comments += num_comments

avg_show_comments = total_show_comments/len(show_posts)
print(avg_show_comments)


# ** Asks posts ** received more comments than **Show posts**. Since ask posts are more likely to receive comments, we'll focus our remaining analysis just on these posts.

# In[12]:


import datetime as dt
result_list = []

for row in ask_posts:
    sub_list = []
    time = row[6]
    num_com = row[4]
    num_com = int(num_com)
    sub_list.append(time)
    sub_list.append(num_com)
    result_list.append(sub_list)

counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    date = row[0]
    comment = row[1]
    date_dt = dt.datetime.strptime(date, "%m/%d/%Y %H:%M")
    hour = date_dt.strftime("%H")
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comment
    else:
        counts_by_hour[hour] +=1
        comments_by_hour[hour] += comment

print(counts_by_hour)
print(comments_by_hour)


# In[15]:


avg_by_hour = []
for hour in counts_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour]/counts_by_hour[hour]])
print(avg_by_hour)


# In[16]:


swap_avg_by_hour = []
for row in avg_by_hour:
    hour = row[0]
    num = row[1]
    swap_avg_by_hour.append([num, hour])
print(swap_avg_by_hour)


# In[20]:


sorted_swap = sorted(swap_avg_by_hour, reverse=True)
print(sorted_swap)


# In[21]:


print(sorted_swap[:5])


# ** On 3PM, 2AM, 8PM, 4PM and 9PM is the best time range for posts to be commented. It is mosly skewed from late afternoon and evening. **

# In[ ]:




