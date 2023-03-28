pipeline {
    agent any
        stages {
            stage('Checkout') {
                steps {
                    git url: 'https://github.com/michaelgaragaty/WorldOfGames.git', branch: 'main'
                }
            }
            stage('Build') {
                steps {
                    sh 'docker-compose build'
                }
            }
            stage('Run') {
                steps {
                    sh 'docker-compose up -d'
                }
            }
            stage('Test') {
                steps {
                    sh 'python tests/e2e.py'
                }
            }
        }
}