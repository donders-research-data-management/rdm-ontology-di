node {

    try {
        stage('Checkout') {
            checkout scm
       }

        stage('Build') {
            sh 'echo "Git hash: `git rev-parse --verify HEAD` , Build on `date`" > build/build.txt'
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
    } catch(Exception e) {
        echo "Got exception: " + e.getMessage() + " -> " + e.toString()
        env.BUILD_FAILURE = e.getMessage()
        throw e
    } finally {
        if (env.BRANCH_NAME == 'release') {
            echo "Mailing release job status"
            def mailRecipients = env.rdmDondersContentMail
            def jobName = currentBuild.fullDisplayName
            
            if (env.BUILD_FAILURE == null) {
                echo "Mailing succes"
                emailext body: '''${SCRIPT, template="groovy-html.template"}''',
                mimeType: 'text/html',
                subject: "[Jenkins] ${jobName}",
                to: "${mailRecipients}",
                replyTo: "${mailRecipients}",
                recipientProviders: [[$class: 'CulpritsRecipientProvider']]
            } else {
                echo "Mailing build failure"
                emailext body: "${jobName} failed: ${env.BUILD_FAILURE}",
                  subject: "[Jenkins] ${jobName}",
                  to: "${mailRecipients}",
                  replyTo: "${mailRecipients}"
            }
        }
    }
}