#!/usr/bin/env python3
import requests
import datetime
import sys
import os
from datetime import datetime, timezone

def check_commits_today(api_repo_url = "https://api.github.com/repos/AsyncStatus/asyncstatus"):
    # GitHub API authentication
    headers = {}
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"
    
    # GitHub API URL for branches
    branches_url = f"{api_repo_url}/branches"
    
    # Get all branches
    response = requests.get(branches_url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching branches: {response.status_code}")
        return False
    
    branches = response.json()
    today = datetime.now(timezone.utc).date()
    
    # Check each branch for commits today
    for branch in branches:
        branch_name = branch["name"]
        commits_url = f"{api_repo_url}/commits?sha={branch_name}&per_page=5"
        
        response = requests.get(commits_url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching commits for branch {branch_name}: {response.status_code}")
            continue
        
        commits = response.json()
        for commit in commits:
            commit_date_str = commit["commit"]["committer"]["date"]
            commit_date = datetime.fromisoformat(commit_date_str.replace("Z", "+00:00")).date()
            
            if commit_date == today:
                print(f"Found commit on branch {branch_name} from today.")
                return True
    
    return False

if __name__ == "__main__":
    print(check_commits_today())
