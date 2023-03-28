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
                    sh 'echo $((0 + $RANDOM % 1000)) > Scores.txt'
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
                    sh 'python3 tests/e2e.py'
                }
            }
            stage('Finalize') {
                steps {
                    sh 'echo 0 > Scores.txt'
                    sh 'docker-compose down'
                    sh 'docker rm -f wog-score-1'
                    sh 'docker-compose push'
                }
            }
        }
}