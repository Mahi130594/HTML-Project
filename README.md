# CI/CD Pipeline for Auto-Deploying HTML Project 
Objective:
Automate the deployment of a static HTML project using GitHub, Python, Bash, Nginx, and Crontab on Linux instance.

## Task 1: Created a Simple HTML Project
📄 Description:A basic HTML page is created to simulate a static website.

📁 Steps:
 - Create a directory named HTML-Project.
 - Inside it, create a file named index.html.
 - Push the project to GitHub repo
## Task 2: Set Up Local Linux Machine with Nginx (on WSL)
 📄 Description: Nginx is installed and configured on the local WSL Linux environment to serve static content.
 - Test: Open http://localhost in your Windows browser to verify that the Nginx welcome page is loading.
 - Purpose: Nginx acts as the web server that hosts the deployed HTML project.
## Task 3: Python Script to Check for New GitHub Commits

📄 Description: This script uses GitHub’s API to fetch the latest commit SHA and compares it with the previously recorded one.

📁 check_commits.py:
 - Purpose: Automates trigger detection for new commits
## Task 4: Bash Script to Deploy the Latest Code
📄 Description: This script clones the latest code from GitHub and copies it to the Nginx web directory.

📁 deploy.sh:
 - Purpose: This is the deployment engine for pulling and serving the latest code.
## Task 5: Set Up a Cron Job
📄 Description: Schedule the Python script to check for updates every 2 minutes.
 - Purpose: Ensures the pipeline checks for new GitHub commits at fixed intervals automatically.
## Task 6: Test the Setup
📄 Description: Make an update to index.html.
 - Push the commit to GitHub.
 - Wait for ~2 minutes.
 - Visit http://localhost and confirm the changes are reflected.
 - Purpose: Validates the full CI/CD pipeline from commit to deployment.
# Result:
### Before HTML File changes
![image](https://github.com/user-attachments/assets/3577e8f2-8c04-4e09-bb8b-591cd15c9857)

### After commit the new HTML File changes
![image](https://github.com/user-attachments/assets/31a231bd-352b-4c2e-981f-bb9279114cfa)

