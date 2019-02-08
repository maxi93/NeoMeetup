#directory with csv file
CSV_DIR="/root/NeoMeetup/Csv"
#neo csv import directory 
NEO_IMPORT="/var/lib/neo4j/import"
#path/to/yourscripts
SCRIPT_DIR="/root/NeoMeetup/CypherScripts"

##useful alias 
#alias=false if no alias required
alias=true 
if $alias
then
if grep "alias cypher" ~/.bashrc
then echo "cypher ok"
else 
    read -p "neo4j pswd: " passwd
    read -p "reimmit pswd: " passwd1
    
    if [ "$passwd0" -a "$passwd1" ]
    then 'echo "alias cypher='cypher-shell -u neo4j -p $PSWD --debug --format verbose'">>~/.bashrc'; source ~/.bashrc  
    else  echo "password doesn't coincide"; exit 
    fi
fi
fi
exit
#SET_COPY=true per copiare i csv nell'import di default di neo
SET_COPY=false
if $SET_COPY 
then echo "sync dirs"; cp  ${CSV_DIR}/*  ${NEO_IMPORT}/
else echo "dir already sync" 
fi

echo "importing members"

cat ${SCRIPT_DIR}/merge_member_from_csv.cql |cypher

echo "importing groups"

cat ${SCRIPT_DIR}/groups_from_csv.cql |cypher

echo "importing events"

cat ${SCRIPT_DIR}/events_from_csv.cql |cypher

echo "importing venues"

cat ${SCRIPT_DIR}/venues_from_csv.cql |cypher



