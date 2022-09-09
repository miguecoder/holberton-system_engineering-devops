#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    all_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    tasks = requests.get(all_url, params={"userId": id}).json()
    num_task = len(tasks)

    name = requests.get(user_url + id).json()
    filter = {"userId": id, "completed": "true"}
    task_completed = requests.get(all_url, params=filter).json()
    num_task_c = len(task_completed)

    print("Employee {} is done with tasks({}/{}):".format(name.get("name"),
          num_task_c, num_task))

    for dic in task_completed:
        for key in dic:
            if key == "title":
                value = dic[key]
                print(f"\t {value}")
    """
        for task in task_completed:
            print("\t {}".format(task.get("title")))
    """
