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
				sh "cd .\Docker\prod\"
				sh "docker-compose up"
                sh "docker build --tag cdrault/tweet-search-project:${version} ."
            }
        }
        
    }
}