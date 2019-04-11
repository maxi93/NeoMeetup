#!/usr/bin/env python
# coding: utf-8

# In[116]:


from __future__ import unicode_literals

import requests
import json
import time
import codecs
import sys

import pandas as pd


# In[117]:


UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


# In[118]:


member_df=pd.read_csv("../Csv/Struttura/member.csv")
#member_df.head()


# In[119]:


member_ids=member_df['member_id']
member_try=[6,7]
#member_ids.head()


# In[120]:


fabri_key="2e12625a12642d6ac743d19566c393e"


# In[121]:


def main():
        #api_key= "2e12625a12642d6ac743d19566c393e"
        #api_key=fabri_key
        api_key= "546938372953301546964e404246e"
        # Get your key here https://secure.meetup.com/meetup_api/key/
        for count,id_ in enumerate(member_ids):
            per_page = 1
            #results_we_got = per_page
            offset = 0
            # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
            response=get_results({"member_id":id_, "key":api_key, "page":per_page, "offset":offset})
            time.sleep(0.1)
            offset += 1
            #results_we_got = response['meta']['count']              
            #time.sleep(1)
            count+=1
            if count is 20:
                break


# In[122]:


def get_results(params):

    request = requests.get("http://api.meetup.com/2/members",params=params)
    data = request.json()
    #print(data)
    #iter_data=json.load(data)
    #a=data['results']
    #print(a)
    #for elem in a:
        #print(elem['topics'])
    print(request)
    return data


# In[123]:


if __name__=="__main__":
        main()


# In[ ]:


## Run this script and send it into a csv:
## python meetup-pages-names-dates.py > meetup_groups.csv

