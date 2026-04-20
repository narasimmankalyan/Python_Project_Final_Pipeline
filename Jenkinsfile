pipeline{
    agent any
    parameters{
        string(name:"Version_name",description:"Provide Application Version")
    }
    stages{
        stage("checkout code"){
            steps{
                
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/narasimmankalyan/Python_Project_Final_Pipeline.git']])
            
            }
        }
        stage("Setup Environment") {
            steps {
                sh '''
                    
                    python3 -m venv murali
                    murali/bin/pip install --upgrade pip
                '''
            }
        }
        stage("Install Dependencies") {
            steps {
                sh '''
                    murali/bin/pip install -r requirements.txt
                    
                '''
            }
        }
                // 🔥 Start MongoDB BEFORE tests
            stage("Start Services") {
                steps {
                    sh '''
                        docker-compose down || true
                        docker-compose up -d mongodb
                        sleep 5
                    '''
                }
            }
        stage("Unit Tests") {
            steps {
                sh '''
                    murali/bin/pytest --maxfail=1 --disable-warnings -v
                '''
            }
        }
        stage("Acceptence"){
            steps{
                
                    input 'proceed'
                
            }
        }
        stage("Building Docker Image"){
            steps{
                sh '''
                 docker build -t my_custom_image:"${Version_name}" .
                '''
            }
        }
        stage("Trivy-to scan-image"){
            steps{
                sh '''
                    trivy image my_custom_image:"${Version_name}"
                '''
            }
        }
        stage("Tagging & Pussing the docker images"){
            steps{
                sh '''
                    docker tag my_custom_image:"${Version_name"}" murali890/my_custom_image:"${Version_name}"
                '''
            }
        }
    }
}
