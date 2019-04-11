#!/usr/bin/env python

# coding: utf-8

# In[116]:


from __future__ import unicode_literals
import sys
import requests
import json
import time
import codecs
import sys

import pandas as pd
import numpy as np

# In[117]:


UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


from itertools import izip
from itertools import izip_longest

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

# In[118]:


member_df=pd.read_csv("../Csv/Struttura/member.csv")
#member_df.head()


# In[119]:
print member_df.head()

member_ids=member_df['member_id']
member_try=[6,9]
#member_ids.head()
member_df['topics']="nan"
#member_df.insert(2, 'topics', np.nan)
#member_ids = pd.Series(np.nan)
#member_df = member_df.assign(e=2)

print member_df.head()
# In[120]:
df_list=np.array_split(member_df, 3)


fabri_key="2e12625a12642d6ac743d19566c393e"
max_key="445811b5a6b424f7e79342826176d"
my_api_key= "546938372953301546964e404246e"
        
block_alert={u'problem': u'Client throttled', u'code': u'throttled', u'details': u'Credentials have been throttled'}

# In[121]:


def main():
        #api_key= "2e12625a12642d6ac743d19566c393e"
        #api_key=fabri_key
        #api_key=max_key
        # Get your key here https://secure.meetup.com/meetup_api/key/
        count=0
        print len(member_df.index)
        #for line in member_df.itertuples():

        #for x, y in pairwise(member_df.itertuples()):
        for z in grouper(member_df.itertuples(),3):
            
            #print x.Index, y.Index
        
            per_page = 1
            #results_we_got = per_page
            offset = 0            
            id_0=member_df.iloc[z[0].Index]['member_id']
            id_1=member_df.iloc[z[1].Index]['member_id']
            id_2=member_df.iloc[z[2].Index]['member_id']

            # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
            response0=get_results({"member_id":id_0, "key":max_key, "page":per_page, "offset":offset})
            response1=get_results({"member_id":id_1, "key":my_api_key, "page":per_page, "offset":offset})
            response2=get_results({"member_id":id_2, "key":fabri_key, "page":per_page, "offset":offset})
            time.sleep(0.17)
            offset += 1
            #results_we_got = response['meta']['count']              
            #time.sleep(1)
            count+=1
           
            data0=response0['results']
            data1=response1['results']
            data2=response2['results']
            
            
            for elem in data0:
                if elem['topics']:
                    print elem['topics']
                    member_df['topics'].at[z[0].Index]=elem['topics']
                print "##########\n###########"
            for elem in data1:
                if elem['topics']:
                    print elem['topics']
                    member_df['topics'].at[z[1].Index]=elem['topics']
                print "##########\n###########"
            for elem in data2:
                if elem['topics']:
                    print elem['topics']
                    member_df['topics'].at[z[2].Index]=elem['topics']
                print "##########\n###########"
        
            if response0 is block_alert:
                break
            if response1 is block_alert:
                break
            if response2 is block_alert:
                break
            print count
            if count is 100:
                break
            
        print member_df.head()
        member_df.to_csv("../Csv/member_enriched.csv")
# In[122]:


def get_results(params):

    request = requests.get("http://api.meetup.com/2/members",params=params)
    data = request.json()
    #print data
    #if count :
    #    print "#####\n dataaa is \n##########"
    #    print data
    #iter_data=json.load(data)
    #a=data['results']
    #print(a)
    #for elem in a:
        #print(elem['topics'])
    #print(request)
    
     
    return data


# In[123]:


if __name__=="__main__":
        main()


# In[ ]:


## Run this script and send it into a csv:
## python meetup-pages-names-dates.py > meetup_groups.csv

