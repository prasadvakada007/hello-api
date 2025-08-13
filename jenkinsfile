// Make this match your actual Docker Hub repo name
def IMAGE_NAME = "yourname/hello-api"
def dockerImage

pipeline {
  agent any
  environment {
    CONTAINER_NAME = "hello-api"
    APP_PORT       = "5000"
  }
  options { timestamps() }
  triggers {
    // Requires the GitHub plugin + a webhook; see step 3
    githubPush()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }

    stage('Login & Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploy (run container)') {
      steps {
        script {
          if (isUnix()) {
            // Linux agents
            sh 'docker rm -f $CONTAINER_NAME || true'
            sh 'docker run -d --restart always --name $CONTAINER_NAME -p $APP_PORT:5000 ' +
               "${IMAGE_NAME}:latest"
          } else {
            // Windows agents (PowerShell)
            powershell '''
              if ((docker ps -aq -f "name=$env:CONTAINER_NAME").Length -gt 0) {
                docker rm -f $env:CONTAINER_NAME | Out-Null
              }
              docker run -d --restart always --name $env:CONTAINER_NAME -p $env:APP_PORT`:5000 `
                ${env:IMAGE_NAME}:latest | Out-Null
            '''
          }
        }
      }
    }
  }

  post {
    always {
      script {
        if (isUnix()) {
          sh 'docker image prune -f'
        } else {
          powershell 'docker image prune -f | Out-Null'
        }
      }
    }
  }
}
