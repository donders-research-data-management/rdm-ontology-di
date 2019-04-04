node {
    try {
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
    } finally {
        deleteDir()
    }
}
