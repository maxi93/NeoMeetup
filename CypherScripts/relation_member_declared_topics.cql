//headers: member_id,group_id,urlkey,topic_name

return "Importing member-declared_topics relations";

USING PERIODIC COMMIT 50000

LOAD CSV WITH HEADERS FROM "file:///relations_topic_with_id.csv" AS row

MATCH (member:Member {id: row.member_id})
MATCH (topic:Topic {id: row.declared_topic_id}) //eventually CHECK and FIX the header!
MERGE (member)-[:DECLARED_INTEREST_IN]->(topic);
       
return "Imported member-declared_topics relations";
