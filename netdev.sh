#!/bin/bash

PUBLIC_IP=$(curl -s https://ipv4.icanhazip.com)

validate="$1"
service="$2"
cloud="$3"
form_factor="$4"
job="$5"

if [ -z "$job" ]; then
  java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s "http://${PUBLIC_IP}:8080" -auth admin:tcs@12345 list-jobs
else
  if [ "$validate" != "full" ] && [ "$validate" != "small" ] && [ "$validate" != "medium" ]; then
    echo "Invalid value for parameter validate: $validate"
    echo "Accepted values are: full, small, or medium"
    exit 1
  fi

  if [ "$cloud" != "Aws" ] && [ "$cloud" != "Azure" ]; then
    echo "Invalid value for parameter cloud: $cloud"
    echo "Accepted values are: Aws or Azure"
    exit 1
  fi

  if [ "$service" != "IMS" ]; then
    echo "Invalid value for parameter service: $service"
    echo "Accepted values are: IMS"
    exit 1
  fi

  if [ "$form_factor" != "CNF" ]; then
    echo "Invalid value for parameter form_factor: $form_factor"
    echo "Accepted values are: CNF"
    exit 1
  fi

  java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s "http://${PUBLIC_IP}:8080" -auth admin:tcs@12345 build "$job" -p validate="$validate" -p service="$service" -p cloud="$cloud" -p form_factor="$form_factor"
  java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s "http://${PUBLIC_IP}:8080" -auth admin:tcs@12345 console "$job"
fi

