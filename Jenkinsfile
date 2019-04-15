node {

    stage('Checkout') {
        checkout scm
   }

    stage('Build') {
        sh 'echo "Git hash: `git rev-parse --verify HEAD` , Build on `date`" > build.txt'
        def branch = env.BRANCH_NAME
        env.TAG = branch.equals('release') ? 'release' : 'latest'
        echo "Building branch ${branch} and pushing as ${env.TAG}"
        dir("build/docker") {
           sh "docker-compose build --no-cache"
           sh "docker-compose push"
       }
    }

    stage('Deploy') {
        if (env.TAG == 'release') {
            echo "Deploying to production"
            sshagent (credentials: ['nonvlinder-credentials']) {
                sh 'ssh "nonvlinder" "/opt/tomcat/rdm-configurable-content-donders/build/docker/start-update.sh"'
            }
        } else {
            echo "Not deploying non release tags"
        }
    }
}