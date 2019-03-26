#!/usr/bin/python
import json
import csv
import ast
from pprint import pprint
from kafka import KafkaConsumer
import time
import pandas as pd
from pandas import DataFrame as df

consumer = KafkaConsumer(bootstrap_servers = 'sandbox-hdf.hortonworks.com:6667',
                         auto_offset_reset = 'earliest',
                         consumer_timeout_ms = 1000)
consumer.subscribe(['project'])
print("subscribed to topic meetup")
messages = []
d = []
start = time.time()
for filename in consumer:
    try:
        j = json.loads(filename.value)
        group_topics = j['group']['group_topics']
        for count, topic in enumerate(group_topics):
            try:
                d.append({'member_id':str(j['member']['member_id']),'group_id':str(j['group']['group_id']),
                             'urlkey':str(topic['urlkey'].encode('utf-8')),'topic_name':str(topic['topic_name'].encode('utf-8'))})
            except Exception as e: 
                print e
                break
    except: 
        print '******Errore*****'
        break
    '''if count==1000:
        print "count is "+str(count)
        break'''

df = pd.DataFrame(d)
df_1 = pd.read_csv("/root/csv/group_topics.csv")
try:
    df_end = df.merge(df_1, how = 'inner', left_on = 'urlkey', right_on = 'urlkey')
except Exception as ex:
    print ex

end = time.time()

print"already wrote "+str(count)+" in "+str(end-start)
print"Time to work on this dataframe!"

df_end.to_csv("/root/csv/relations_topics_try.csv", index = False)
print(len(df))

