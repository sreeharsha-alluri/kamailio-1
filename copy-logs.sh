#!/bin/bash 
for i in $(docker exec -it sipp sh -c "ls *.csv") 
do
#echo $i
docker cp sipp:/$i ./ 2>/dev/null
done
