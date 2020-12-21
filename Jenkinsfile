def version = "0.1-dev";

pipeline {
    agent any
    stages {
        
        stage('Build Docker images') {
            when{
                anyOf{
                    branch 'dev'
                }
            }
            steps {
				sh "echo docker up"
            }
        }
        
    }
}