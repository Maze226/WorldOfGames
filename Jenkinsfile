pipeline {
    agent any
        stages {
            stage('Checkout') {
                steps {
                    git url: 'https://github.com/michaelgaragaty/WorldOfGames.git' branch: 'main'
                }
            }
            stage('Build') {
                steps {
                    sh 'docker-compose build'
                }
            }
        }
}