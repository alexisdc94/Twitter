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
				bat "docker build -t twitterapp ."
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
                bat "docker stop tweet_app_search"
                bat "docker rm tweet_app_search"
                bat "docker run -d -p 5000:5000 --name tweet_app_search twitterapp"
            }
        }
		
    }
}