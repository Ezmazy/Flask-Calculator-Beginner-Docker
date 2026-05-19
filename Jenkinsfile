pipeline {
    agent any

    environment {
        IMAGE_NAME     = "flask-calculator"
        CONTAINER_NAME = "flask-calculator-app"
        APP_PORT       = "5000"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '>>> Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '>>> Building Docker image...'
                sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                    echo "Image built: ${IMAGE_NAME}:${BUILD_NUMBER}"
                '''
            }
        }

        stage('Test') {
            steps {
                echo '>>> Running Python unit tests inside Docker container...'
                sh '''
                    docker run --rm \
                        --name ${IMAGE_NAME}-test \
                        ${IMAGE_NAME}:latest \
                        python -m pytest test_app.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '>>> Deploying application...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm   ${CONTAINER_NAME} || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:5000 \
                        ${IMAGE_NAME}:latest
                    echo "App is running at http://localhost:${APP_PORT}"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline SUCCESS — Flask Calculator is live on port 5000!'
        }
        failure {
            echo 'Pipeline FAILED — check the stage logs above.'
        }
    }
}
