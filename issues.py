import requests
import sys
import os

# GitHub API endpoint for creating issues
issues_url = "https://api.github.com/repos/the2dl/REPONAME/issues"

# Obtain your Personal Access Token from https://github.com/settings/tokens
headers = {
    "Authorization": "token INSERT_TOKEN"
}

# Check if a filename was provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: ./issues.py <filename.md>")
    sys.exit(1)

filename = sys.argv[1]

# Extract the filename without extension
base_filename = os.path.splitext(filename)[0]

# Format the title
title = "New content creation for {}".format(base_filename)

# Read the Markdown file
with open(filename, "r") as f:
    content = f.read()

# Prepare the issue data
data = {
    "title": title,
    "body": content
}

# Send the POST request to create the issue
response = requests.post(issues_url, headers=headers, json=data)

if response.status_code == 201:
    print("Issue created successfully!")
    print("Issue URL:", response.json()["html_url"])
else:
    print("Error creating issue:", response.text)
