node('slave1'){
    stage('cloning'){
        sh "rm -rf *"
        // sh 'git clone https://github.com/sreeharsha-alluri/Test.git'
        sh 'git clone https://github.com/DaggupatiPavan/kamailio.git' 
        sh "sudo sed -i 's/-1.0/-1.${BUILD_NUMBER}/g' /home/ubuntu/jenkins/workspace/kaniko-dockerhub/kamailio/Test.yaml"
        sh 'pwd'
    }
    stage('Build and push'){
        sh "kubectl delete pod kaniko"
        sh 'kubectl apply -f /home/ubuntu/jenkins/workspace/kaniko-dockerhub/kamailio/Test.yaml'
        sh 'sleep 220'
    }
    stage('Vulnerability Scan for Docker images'){
        sh "docker pull kgopi424/kamailio:v-1.${BUILD_NUMBER}"
        sh 'grype kgopi424/kamailio:v-1.${BUILD_NUMBER}'
    }
    stage('Docker image Build and Run'){
        // sh 'sudo docker build -t kamailio kamailio/.'
        sh 'sudo docker rm -f kamailio'
        sh 'sudo docker run -itd --network=host --name kamailio kgopi424/kamailio:v-1.${BUILD_NUMBER}'
        sh 'sleep 5'
        sh 'bash kamailio/modify.sh'
        sh 'sudo docker stop kamailio'
        sh 'sudo docker start kamailio'
    }
    
}
