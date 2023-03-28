pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/michaelgaragaty/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t wog-score .'
            }
        }
    }
}