pipeline {
    agent any

    environment {
        // Use a virtualenv inside the workspace so each build is isolated
        VENV_DIR = "${WORKSPACE}\\.venv"
    }

    stages {

        stage('Checkout') {
            steps {
                // Jenkins checks out the repo automatically when using SCM.
                // This echo is just a learning marker.
                echo "Source code checked out to: ${WORKSPACE}"
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip'
                bat '%VENV_DIR%\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '%VENV_DIR%\\Scripts\\playwright install chromium'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '''
                    %VENV_DIR%\\Scripts\\pytest tests/ ^
                        --browser chromium ^
                        --junitxml=test-results/results.xml ^
                        -v
                '''
            }
            post {
                always {
                    // Publish JUnit results in Jenkins so you can see pass/fail
                    junit 'test-results/results.xml'
                }
            }
        }
    }

    post {
        success { echo 'All tests passed!' }
        failure { echo 'Some tests failed. Check the test results above.' }
    }
}
