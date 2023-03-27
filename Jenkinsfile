pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://github.com/michaelgaragaty/WorldOfGames.git']])
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t wog-score .'
            }
        }
    }
}