pipeline {
    agent { label 'slave1' }
    parameters {
        string(name: 'validate', defaultValue: 'full', description: 'Validation level')
        string(name: 'service', defaultValue: 'IMS', description: 'Service')
        choice(name: 'cloud', choices: ['Azure', 'Aws'], description: 'Cloud provider')
        string(name: 'form_factor', defaultValue: 'CNF', description: 'Form factor')
    }
    stages {
        stage('validation'){
            steps{
                script{
                    if(params.validate == "full" && params.service == "IMS" && (params.cloud == "Aws" || params.cloud == "Azure") && params.form_factor == "CNF"){
                        echo "Build is Running"
                    }
                    else {
                         error("Build failed due to incorrect parameter, stopping pipeline")
                    }
                }
            }
        }
        stage('Cloning') {
            steps {
                sh "rm -rf .git"
//                 sh "git clone https://github.com/DaggupatiPavan/kamailio.git ./" 
                sh "sudo sed -i 's/-1.0/-1.${BUILD_NUMBER}/g' /home/ubuntu/jenkins/workspace/${env.JOB_NAME}/Test.yaml"
                sh "sudo sed -i 's/kamailio-jenkinss-cli/${env.JOB_NAME}/g' /home/ubuntu/jenkins/workspace/${env.JOB_NAME}/NetDevOps"
                sh "sudo sed -i 's/kamailio-jenkinss-cli/${env.JOB_NAME}/g' /home/ubuntu/jenkins/workspace/${env.JOB_NAME}/NetDevOps.py"
                sh 'pwd'
            }
        }
        stage('Build and push'){
            steps {
                sh "kubectl delete pod kaniko"
                sh "kubectl apply -f /home/ubuntu/jenkins/workspace/${env.JOB_NAME}/Test.yaml"
                sh 'sleep 180'
            }
        }
        stage('Vulnerability Scan for Docker images'){
            steps {
                sh "docker pull kgopi424/kamailio:v-1.${BUILD_NUMBER}"
                sh "grype kgopi424/kamailio:v-1.${BUILD_NUMBER}"
            }
        }
        stage('Docker image Build and Run'){
            steps {
                sh "sudo docker rm -f kamailio"
                sh "sudo docker run -itd --network=host --name kamailio kgopi424/kamailio:v-1.${BUILD_NUMBER}"
                sh 'sleep 5'
                sh 'bash modify.sh'
                sh 'sudo docker stop kamailio'
                sh 'sudo docker start kamailio'
            }
        }
    }
}

