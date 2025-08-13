pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t prasadvakada007/hello-api .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker push prasadvakada007/hello-api'
            }
        }
    }
}


