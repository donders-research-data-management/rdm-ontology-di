node {
    // Determine image tag to push to. For dr environments use a '-donders' suffix.
    def branch = env.BRANCH_NAME
    def tagSuffix = ''
    def rdrEnvironment = 'rdr'
    def environmentPrefix = rdrEnvironment
    if (branch.startsWith('dr')) {
        tagSuffix = '-donders'
        environmentPrefix = 'dr'
    }
    def tag = 'docker.isc.ru.nl/rdr/web/rdr-configurable-content' + tagSuffix

    // Determine image version to push, release if contains release else latest
    def version = 'latest'
    def dtap = 'acc'
    if (branch.contains('release')) {
       version = 'release'
       dtap = 'prod'
    }

    def subjectResult = 'deployed successfully'
    try {
        stage('Checkout') {
            checkout scm
        }

        stage('Build') {
            sh 'echo "Git hash: `git rev-parse --verify HEAD` , Build on `date`" > build/build.txt'
            // Build image and push based on tag and version determined from branch
            echo "Building branch ${branch} and pushing as ${tag}:${version}"
            sh "docker build -f build/docker/Dockerfile -t ${tag}:${version} --no-cache --pull=true ."
            sh "docker push ${tag}:${version}"
        }

        stage('Deploy') {
            def ccDir = "/data/rdr/rdr-configurable-content-deployment"
            // Determine environment to deploy to based on environment and dtap determined from branch
            def environment = environmentPrefix + '-' + dtap + '-portal'
            echo "Deploying branch ${branch} of configurable content to ${environment}"
            sshagent (credentials: ['rdr-jenkins-ssh-credentials']) {
                sh "ssh ${environment} $ccDir/start-update.sh ${version}"
            }
        }

    } catch(Exception e) {
        echo "Exception caught: " + e.getMessage() + " -> " + e.toString()
        // Make the email send a failure message, and set the subject appriopriately
        currentBuild.result = 'FAILURE'
        subjectResult = 'build failed'
        throw e
    } finally {
        echo "Mailing release job status"
        def recipients = environmentPrefix.equals(rdrEnvironment) ? env.configurableContentRecipientsRdr :
            env.configurableContentRecipientsDr
        def jobName = currentBuild.fullDisplayName
        def subject = 'RDR content '
        body = '''${SCRIPT, template="groovy-html.template"}'''
        subject += subjectResult

        emailext body: body,
            mimeType: 'text/html',
            subject: subject,
            from: 'RDR buildserver',
            to: recipients,
            replyTo: env.supportEmailRdr,
            recipientProviders: [[$class: 'CulpritsRecipientProvider']]
    }
}
