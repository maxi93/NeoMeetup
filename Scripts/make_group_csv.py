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
messages = []
groups= {}
for count, filename in enumerate(consumer):
	#print filename
	#filename=path+filename
	#with open(filename) as file:  
		#data = file.read()
		#print data
	try:        
	        j = json.loads(filename.value)
		group_id = j['group']['group_id']
       		try:
			if group_id not in groups:
	       			groups[group_id]= ast.literal_eval(json.dumps(j['group']))
				#groups[group_id].pop("group_id")             
       		except Exception, ex:
       			print("inner for")
       			print ex
	except Exception, e:
       		print("outer for")
       		print e

	if count==100000:
	        print "count is "+str(count)
	        break
          

print "################"
print "processed messages: "+str(count+1)
print " names dict lenght: "+str(len(groups))

#print groups
#pprint(groups)
with open('/root/csv/group_topics.csv', 'wb') as f:  
	fields=["group_id","group_city","group_country","group_lat","group_lon","group_name","group_state","group_topics","group_urlname"]
	w = csv.DictWriter(f, fields)
	w.writeheader()
	for k in groups:
		w.writerow({field: groups[k].get(field) or "NONE" for field in fields})
