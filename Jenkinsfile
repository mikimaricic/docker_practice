pipeline {
    agent { dockerfile true }
    stages {
        stage('Build image') {
            steps {
                echo 'Starting to build docker image ..'

                sh 'node --version'
                sh 'svn --version'
            }
        }
        stage('test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('log') {
            steps {
                println "Hello World"
            }
        }
    }
}
