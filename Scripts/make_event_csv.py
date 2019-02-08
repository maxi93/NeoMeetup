#!/usr/bin/python
import json
import csv
import ast
from pprint import pprint
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers = 'sandbox-hdf.hortonworks.com:6667',
                         auto_offset_reset = 'earliest',
                         consumer_timeout_ms = 1000)
consumer.subscribe(['project'])
print("subscribed to topic meetup")
events= {}
for count, filename in enumerate(consumer):
    try:
        j = json.loads(filename.value)
        event_id = j['event']['event_id']
        try:
            if event_id not in events:
                events[event_id]= ast.literal_eval(json.dumps(j['event']))           
        except Exception, ex:
       			print("inner for")
       			print ex
    except Exception, e:
       		print("outer for")
       		print e

    '''if count==9:
        print "count is "+str(count)
        break'''
          
#pprint(events)
print "################"
print "processed messages: "+str(count+1)
print " names dict lenght: "+str(len(events))

with open('/root/meetup_stuffs/event.csv', 'wb') as f:  
	fields=["event_id","event_name","event_url","time"]
	w = csv.DictWriter(f, fields)
	w.writeheader()
	for k in events:
		w.writerow({field: events[k].get(field) or "NONE" for field in fields})