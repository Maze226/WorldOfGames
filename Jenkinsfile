pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'git clone https://github.com/michaelgaragaty/WorldOfGames.git'
                sh 'cd WorldOfGames'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t wog-score .'
            }
        }
    }
}