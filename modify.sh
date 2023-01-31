#!/bin/bash 

hostname -I | cut -d " " -f 1 > PRI_IP
curl ifconfig.me > PUB_IP
echo "listen=udp:$(cat PRI_IP):5060 advertise $(cat PUB_IP):5060" >> kam.cfg
echo "listen=tcp:$(cat PRI_IP):5060 advertise $(cat PUB_IP):5060" >> kam.cfg
echo "alias=localhost:5060" >> kam.cfg
echo "auto_aliases=no" >> kam.cfg 
echo "advertised_address=$(cat PUB_IP)" >> kam.cfg 


sudo docker cp kam.cfg kamailio:/etc/kamailio/kamailio.cfg 

sudo docker cp kamailio kamailio:/etc/default/kamailio 


