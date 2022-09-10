#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests


if __name__ == "__main__":

    all_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(user_url).json()

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({i.get("id"): [{
            "task": tt.get("title"),
            "completed": tt.get("completed"),
            "username": i.get("username")}
            for tt in requests.get(all_url, params={
                "userId": i.get("id")}).json()]
            for i in users}, outfile)
