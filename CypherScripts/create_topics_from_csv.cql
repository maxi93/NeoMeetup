return "Importing topics";

CREATE INDEX ON :Topic(id);

LOAD CSV WITH HEADERS FROM "file:///relations_topic_with_id.csv" AS row
WITH DISTINCT row.urlkey AS urlkey, row.topic_name AS name, row.topic_id AS id
MERGE (topic:Topic {id: id})
ON CREATE SET topic.name = name,
              topic.urlkey = urlkey;
       
return "Imported topics";
