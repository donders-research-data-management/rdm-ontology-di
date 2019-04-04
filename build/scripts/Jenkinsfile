node {
    def mvnHome = tool 'M3'
    try {
        stage('Checkout') {
            checkout scm
        }

        stage('Build') {
            sh 'printenv'
            sh 'echo "Git hash: `git rev-parse --verify HEAD` , Build on `date`" > build.txt'
            def branchDetachedHead = env.BRANCH_NAME
            def branch = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
            echo "Branch is ${branch} detached head ${branchDetachedHead}"
            branch = branchDetachedHead == null ? branch : branchDetachedHead
            echo "Branch is ${branch}"
            sh "make dist"
            env.TAG = branch.equals('master') ? 'latest' : branch
            dir("tools/docker") {
                sh "docker-compose build"
                sh "docker-compose push"
            }
        }

        stage('Archive') {
			archiveArtifacts artifacts: '**/rdm-configurable-content-*', fingerprint: true
        }
    } finally {
        deleteDir()
    }
}