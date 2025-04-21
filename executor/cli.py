#!/usr/bin/env python3
import typer
import requests
from datetime import datetime, timezone
from github_repo.read_git_repo_status import check_commits_today
from github_repo.delete_git_repo import delete_github_repository
import sys
import os

app = typer.Typer(help="CLI tool to check GitHub repository activity")

@app.command()
def check_repo():
    """
    Check if there were any commits made today on any branch of the GitHub repository.
    """
    result = check_commits_today()
    if result:
        print("Repository has activity today")
    else:
        # delete_github_repository()
        print("Repository deleted")


if __name__ == "__main__":
    app()
