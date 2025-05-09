#!/usr/bin/env python3

import requests
import os

REPO = "Mahi130594/HTML-Project"
BRANCH = "master"
TOKEN = "ghp_your_github_token_here"  # Replace with your actual GitHub personal access token
LAST_COMMIT_FILE = "/home/ubuntu/HTML-Project/last_commit.txt"
DEPLOY_SCRIPT = "/home/ubuntu/HTML-Project/deploy.sh"

headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    latest_commit = response.json()["sha"]
except Exception as e:
    print(f"Failed to fetch commit: {e}")
    exit(1)

# Read previous commit SHA
if os.path.exists(LAST_COMMIT_FILE):
    with open(LAST_COMMIT_FILE, "r") as f:
        last_commit = f.read().strip()
else:
    last_commit = ""

# Compare and deploy
if latest_commit != last_commit:
    print("New commit detected. Running deployment...")
    os.system(f"bash {DEPLOY_SCRIPT}")
    with open(LAST_COMMIT_FILE, "w") as f:
        f.write(latest_commit)
else:
    print("No new commit found.")
