pipeline {
    agent any
    stages {
        stage('Build Docker images') {
            when{
                anyOf{
                    branch 'dev'
                    branch 'feature'
                }
            }
            steps {
				sh "docker build -t twitterapp ."
            }
        }
        
		stage('Launch app on server') {
            when{
                anyOf{
                    branch 'dev'
					branch 'release'
                }
            }
            steps {
                sh "docker stop tweet_app_search"
                sh "docker rm tweet_app_search"
                sh "docker run -d -p 5000:5000 --name tweet_app_search twitterapp"
            }
        }
		
    }
}