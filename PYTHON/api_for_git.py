# API for to access data from Git Repository

import requests

url = "https://api.github.com/users/RatnaKadam/repos"

response = requests.get(url)

repos = response.json()

if response.status_code == 200:
    for repo in repos:
        print(f"Repository Name: {repo['name']}")
else:
    print(f"Something went wrong. The status code is {response.status_code}")