pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    parameters {
                string(name: 'COMPONENT_NAME', defaultValue: 'Kafka')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building in integration...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing in integration...'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver in integration...'
            }
        }
    }
}
