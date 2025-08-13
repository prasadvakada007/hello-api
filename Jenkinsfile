pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Docker Login') {
            steps {
                bat "docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t prasadvakada007/hello-api:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker push prasadvakada007/hello-api:latest'
            }
        }
    }
}



