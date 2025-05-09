#!/bin/bash

REPO_URL="https://github.com/Mahi130594/HTML-Project.git"
TMP_DIR="/tmp/HTML-Project"
DEPLOY_DIR="/var/www/html"
LOG_FILE="/home/ubuntu/HTML-Project/deploy.log"

echo "------ Deployment Started: $(date) ------" >> $LOG_FILE

# Clean temp directory
rm -rf $TMP_DIR
git clone $REPO_URL $TMP_DIR >> $LOG_FILE 2>&1

# Deploy HTML file
sudo cp $TMP_DIR/index.html $DEPLOY_DIR >> $LOG_FILE 2>&1

# Restart nginx
sudo systemctl restart nginx >> $LOG_FILE 2>&1

echo "Deployment completed successfully at $(date)" >> $LOG_FILE
