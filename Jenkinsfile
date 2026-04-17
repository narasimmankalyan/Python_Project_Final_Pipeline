
pipeline{
    agent any
    stages{
        stage("checkout code"){
            steps{
                
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/narasimmankalyan/Python_Project_Final_Pipeline.git']])
            
            }
        }
    }
}
