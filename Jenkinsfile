pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'http://github.com/michaelgaragaty/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
    }
}