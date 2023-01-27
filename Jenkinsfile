node ('kamailio'){
    stage('Clone'){
        sh 'rm -rf *'
        sh 'git clone https://github.com/DaggupatiPavan/kamailio.git' 
    }
    stage('Docker image Build and Run'){
        sh 'sudo docker build -t kamailio kamailio/.'
        sh 'sudo docker rm -f kamailio'
        sh 'sudo docker run -itd --network=host --name kamailio kamailio'
        sh 'sleep 5'
        sh 'bash kamailio/modify.sh'
    }
}
