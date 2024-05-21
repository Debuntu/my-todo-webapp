pipeline {
	agent any
	options {
        skipStagesAfterUnstable()
	}
	stages {
		stage('Build') {
			steps {
				sh 'python -m py_compile sources/web.py sources/functions.py'
				stash(name: 'compiled_results', includes: 'sources/*.py*')
			}
		}
		stage('Test') {
			steps {
				sh 'py.test --junit-xml test-reports/results.xml sources/functions.py'
			}
			post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') { 
            steps {
                sh "pyinstaller --onefile sources/web.py" 
            }
            post {
                success {
                    archiveArtifacts 'dist/web' 
                }
            }
        }
	}
}