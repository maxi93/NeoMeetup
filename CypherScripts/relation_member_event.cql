//headers: member_id,event_id,response

return "Importing member-event relations";

LOAD CSV WITH HEADERS FROM "file:///relations_members-events-response[new].csv" AS row
MATCH (member:Member {id: row.member_id})
MATCH (event:Event {id: row.event_id})
MERGE (member)-[:WILL_PARTECIPATES {response: row.response, guests: row.guests}]->(event);
       
return "Imported member-event-response relations";