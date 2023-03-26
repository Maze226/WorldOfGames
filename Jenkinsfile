pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git checkout 'https://github.com/michaelgaragaty/WorldOfGames'
            }
        }
        stage('Build') {
            steps {
                docker -t wog-docker .
            }
        }
        stage('Run') {
            steps {
                docker-compose up
            }
        }
        stage('Test') {
            steps {
                echo 'hello world!'
            }
        }
        stage('Finalize') {
            steps {
                echo 'hello world!'
            }
        }
    }
}