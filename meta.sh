#keeping this as simple as possible, we can run the below command to get data in JSOn format 

curl --silent http://169.254.169.254/latest/dynamic/instance-identity/document

#TO get required value use below command while running this script 

#sh meta.sh | jq -r .instanceId  #fetches Instance Id , Screenshots attached in readme 
