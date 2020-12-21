def version = "0.1-dev";

pipeline {
    agent any
    stages {
        
        stage('Build Docker images') {
            when{
                anyOf{
                    branch 'features'
                }
            }
            steps {
				sh "echo hi"
            }
        }
        
    }
}