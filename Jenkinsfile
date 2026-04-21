pipeline{
    agent any
    environment{
        Docker_hub_credientials=credentials("dockerhub")
    }
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
                        docker compose down || true
                        docker compose up -d mongodb
                        sleep 5
                    '''
                }
            }
        stage("Unit Tests") {
            environment {
                MONGODB_HOST = "localhost"
                MONGODB_PORT = "27018"
                MONGODB_DBNAME = "studentdb"
                MONGODB_USERNAME = "admin"
                MONGODB_PASSWORD = "testtesttest"
            }
            steps {
                sh '''
                    murali/bin/pytest --maxfail=1 --disable-warnings -v
                '''
            }
}
           
            stage("Stop Services"){
                steps{
                    sh '''
                        docker compose down
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
        stage("Tagging docker images"){
            steps{
                sh '''
                    docker tag my_custom_image:"${Version_name}" murali890/my_custom_image:"${Version_name}"
                '''
            }
        }
        stage("Logging in to Docker hub and Pushing"){
            steps{
                sh '''
                    docker login -u $Docker_hub_credientials_USR --password $Docker_hub_credientials_PSW
                    echo "logging in to docker hub and pusshing the images to the docker hub"
                    docker push murali890/my_custom_image:"${Version_name}"
                '''
            }
        }
        stage("Deploy Application"){
    steps{
        sh '''
            echo "Starting deployment..."

            # Set version for docker-compose
            export STUDENT_STORE_APP_TAG=${Version_name}

            # Stop old containers (if any)
            docker compose down || true

            # Pull latest image from DockerHub
            docker compose pull

            # Start containers in background
            docker compose up -d

            echo "Deployment completed successfully 🚀"
        '''
    }
}
        
    }
}
