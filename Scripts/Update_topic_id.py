#!/usr/bin/python
import json
import csv
import ast
from pprint import pprint
#from kafka import KafkaConsumer
import time
import pandas as pd
from pandas import DataFrame as df


# In[9]:


start_t=time.time()


# In[10]:


df = pd.read_csv("..csv/struttura/relations_topics.csv")


# In[11]:


df.head()


# In[12]:


df1= pd.read_csv("..csv/struttura/member_enriched.csv")


# In[13]:


df1=df1.drop(columns='Unnamed: 0')


# In[14]:


#df1.head()


# In[15]:


df1.dropna(inplace=True)


# In[16]:


id_list=[]
topic_list=[]
setcount=None
for count,line  in enumerate(df1.itertuples()):
    topics=df1.topics[line.Index]
    tmp_list=topics.split()
    
    for elem in tmp_list:
        #print(line.Index)
        id_list.append(df1['member_id'][line.Index])
        elem=elem.strip("[").strip("]").strip(",")
        elem=elem.replace("'","")
        topic_list.append(elem)
    if setcount:        
        if count is 2:
            break


# In[17]:


df2=pd.DataFrame({"type":1,"group_id":"NaN","member_id":id_list,"topic_name":"NaN","urlkey":topic_list})
#print(len(df2))
df2.head()


# In[18]:


df['type']=0
df['type']=df['type'].apply(int)


# In[19]:


df_c=pd.concat([df, df2], sort=False)
df_c.head()


# In[20]:


df_c.tail()


# In[21]:


#print(len(df_c))
#print(len(df2))
#print(len(df))
#print("sum len:"+str(len(df)+len(df2)))


# In[22]:


del df


# In[23]:


del df1
del df2


# In[24]:


df_c.sort_values('urlkey', inplace=True)
#df.head()


# In[25]:


df_c.reset_index(inplace=True)


# In[26]:


df_c.drop('index', axis=1, inplace=True)


# In[27]:


df_c['topic_id']=0

temp=df_c.urlkey.at[0]
count=0
index=0


for line in df_c.itertuples():

    curr_url=line.urlkey
    if curr_url == temp:
        df_c['topic_id'].at[line.Index]=count

    else:
        count+=1
        df_c['topic_id'].at[line.Index]=count
        temp=curr_url
    #if count == 20:
    #    break
    


# In[28]:


# In[9]:


df_c.head(50)


# In[29]:


# In[10]:


# In[30]:


#df_create_topic=pd.DataFrame([df_c['topic_id'],df_c['urlkey']])
df_create_topic=pd.concat([df_c['topic_id'],df_c['urlkey']], axis=1).reset_index() #eventually add topic_name


# In[ ]:


df_create_topic.head(50)


# In[34]:


df_create_topic.to_csv("../csv/struttura/Create_topic_nodes.csv", index=False)


# In[35]:


del df_create_topic


# In[ ]:


df_topic_interest=df_c[df_c['type']==0]


# In[ ]:


df_topic_interest.drop(columns='type', inplace=True)


# In[40]:


df_topic_interest.to_csv("../csv/struttura/relations_topics_with_id.csv", index=False)


# In[41]:


del df_topic_interest


# In[44]:


df_topic_decleared=df_c[df_c['type']==1]
df_topic_decleared.drop(columns=['type','group_id','topic_name'], inplace=True)


# In[46]:


df_topic_decleared.to_csv("../csv/struttura/relations_decleared_topics.csv", index=False)


# In[ ]:





# In[ ]:

time=(time.time()-start_t)/60
print "completed in "+str(time)+" minutes"


