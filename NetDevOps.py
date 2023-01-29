import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--validate", required=True)
parser.add_argument("--service", required=True)
parser.add_argument("--cloud", required=True)
parser.add_argument("--form_factor", required=True)
args = parser.parse_args()

# Get public IP
response = requests.get("https://ipv4.icanhazip.com")
public_ip = response.text.strip()

# Check if cloud parameter is valid
if args.cloud not in ["Aws", "Azure"]:
    print(f"Invalid value for parameter cloud: {args.cloud}")
    print("Accepted values are: Aws or Azure")
    exit(1)

# Execute the Jenkins CLI commands with the provided IP and parameters
os.system(f"java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s http://{public_ip}:8080 -auth admin:tcs@12345 build kamailio-jenkinss-cli -p validate={args.validate} -p service={args.service} -p cloud={args.cloud} -p form_factor={args.form_factor}")
os.system(f"java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s http://{public_ip}:8080 -auth admin:tcs@12345 console kamailio-jenkinss-cli")
