pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building..'
            }
        }
        stage('test') {
            steps {
                echo 'Testing..'
            }
            steps {
                echo 'Validation..'
            }
        }
        stage('log') {
            steps {
                println "Hello World"
            }
        }
    }
}
