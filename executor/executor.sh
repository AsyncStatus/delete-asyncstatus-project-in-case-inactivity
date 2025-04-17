#!/bin/bash

echo "LOL"
REPO_URL="https://github.com/AsyncStatus/asyncstatus.git"
TODAY=$(date +%Y-%m-%d)

check_repo_activity() {
    if git ls-remote --exit-code "$REPO_URL" &>/dev/null; then
        LAST_COMMIT_DATE=$(git ls-remote --refs "$REPO_URL" | awk '{print $2}' | xargs -I {} git log -1 --format=%ci {} | cut -d' ' -f1)
        if [[ "$LAST_COMMIT_DATE" == "$TODAY" ]]; then
            echo "true"
        else
            echo "false"
        fi
    else
        echo "false"
    fi
}

check_repo_activity
