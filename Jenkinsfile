pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               sh 'git clone https://github.com/michaelgaragaty/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
    }
}