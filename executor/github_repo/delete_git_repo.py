#!/usr/bin/env python3
import requests
import os
import sys
from typing import Optional, Tuple

def delete_github_repository(
    repo_url: str = "https://api.github.com/repos/AsyncStatus/asyncstatus",
    token: Optional[str] = None
) -> Tuple[bool, str]:
    """
    Delete a GitHub repository using the GitHub API.
    
    Args:
        repo_url (str): The API URL of the repository to delete, e.g.,
                       "https://api.github.com/repos/AsyncStatus/asyncstatus"
        token (str, optional): GitHub personal access token with delete_repo permission.
                              If not provided, will try to get from GITHUB_TOKEN environment variable.
    
    Returns:
        Tuple[bool, str]: A tuple containing (success, message)
        - success: True if deletion was successful, False otherwise
        - message: A descriptive message of the result
    """
    # Extract owner and repo name from URL
    if not repo_url.startswith("https://api.github.com/repos/"):
        return False, "Invalid repository URL format. Expected format: https://api.github.com/repos/owner/repo"
    
    path_parts = repo_url.split('/')
    if len(path_parts) < 6:
        return False, "Invalid repository URL. Could not extract owner and repository name."
    
    owner = path_parts[4]
    repo_name = path_parts[5]
    
    # Get token from environment if not provided
    if not token:
        token = os.environ.get('GITHUB_TOKEN')
        if not token:
            return False, "No GitHub token provided. Set GITHUB_TOKEN environment variable or pass token parameter."
    
    # Set up the request headers
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Make the DELETE request
    response = requests.delete(repo_url, headers=headers)
    
    # Check the response
    if response.status_code == 204:
        return True, f"Repository {owner}/{repo_name} was successfully deleted."
    elif response.status_code == 404:
        return False, f"Repository {owner}/{repo_name} not found or you don't have permission to delete it."
    elif response.status_code == 403:
        return False, f"Insufficient permissions to delete repository {owner}/{repo_name}. Ensure your token has the delete_repo scope."
    else:
        return False, f"Failed to delete repository. Status code: {response.status_code}, Response: {response.text}"

if __name__ == "__main__":
    # Example usage
    repo_url = "https://api.github.com/repos/AsyncStatus/asyncstatus"
    
    # Get token from environment variable
    token = os.environ.get('GITHUB_TOKEN')
    
    if len(sys.argv) > 1:
        repo_url = sys.argv[1]
    
    success, message = delete_github_repository(repo_url, token)
    print(message)
    sys.exit(0 if success else 1)
