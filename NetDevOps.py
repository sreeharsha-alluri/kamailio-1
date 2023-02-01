import os
import argparse
import requests

# Get the public IP address
response = requests.get('https://ipv4.icanhazip.com')
PUBLIC_IP = response.text.strip()

# Parse input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--validate', required=True)
parser.add_argument('--service', required=True)
parser.add_argument('--cloud', required=True)
parser.add_argument('--form_factor', required=True)
args = parser.parse_args()

# Validate input parameters
if args.validate not in ['full', 'small', 'medium']:
    print("Invalid value for parameter validate: {}".format(args.validate))
    print("Accepted values are: full, small, or medium")
    exit(1)

if args.cloud not in ['Aws', 'Azure']:
    print("Invalid value for parameter cloud: {}".format(args.cloud))
    print("Accepted values are: Aws or Azure")
    exit(1)

if args.service != 'IMS':
    print("Invalid value for parameter service: {}".format(args.service))
    print("Accepted values are: IMS")
    exit(1)

if args.form_factor != 'CNF':
    print("Invalid value for parameter form_factor: {}".format(args.form_factor))
    print("Accepted values are: CNF")
    exit(1)

# Execute the Jenkins CLI commands with the provided IP and parameters
os.system(f"java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s http://{public_ip}:8080 -auth admin:tcs@12345 build kamailio-jenkinss-cli -p validate={args.validate} -p service={args.service} -p cloud={args.cloud} -p form_factor={args.form_factor}")
os.system(f"java -jar /home/ubuntu/jenkins/jenkins-cli.jar -s http://{public_ip}:8080 -auth admin:tcs@12345 console kamailio-jenkinss-cli")
