#!/usr/bin/python3
"""Python script that, using this REST API"""
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    all_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    tasks = requests.get(all_url, params={"userId": id}).json()
    num_task = len(tasks)

    name = requests.get(user_url + id).json().get("name")
    filter = {"userId": id, "completed": "true"}
    task_completed = requests.get(all_url, params=filter).json()
    num_task_c = len(task_completed)

    print("Employee {} is done with tasks({}/{}):"
          .format(name,
                  num_task_c, num_task))

    for task in task_completed:
        print("\t {}".format(task.get("title")))
