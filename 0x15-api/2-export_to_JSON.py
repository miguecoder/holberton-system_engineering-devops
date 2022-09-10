#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    all_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    tasks = requests.get(all_url, params={"userId": id}).json()
    name = requests.get(user_url + id).json().get("username")

    with open(id + '.json', 'w') as outfile:
        json.dump({id: [{"task": tt.get("title"), "completed": tt.get(
            "completed"), "username": name} for tt in tasks]}, outfile)
