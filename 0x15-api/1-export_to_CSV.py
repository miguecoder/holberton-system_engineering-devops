#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]
    all_url = "https://jsonplaceholder.typicode.com/todos/"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    tasks = requests.get(all_url, params={"userId": id}).json()
    num_task = len(tasks)
    name = requests.get(user_url + id).json().get("username")

    with open(id + '.csv', 'w') as filecvs:
        writer = csv.writer(filecvs, quoting=csv.QUOTE_ALL)
        for title in tasks:
            a = [id] + [name] + [title.get("completed")]
            b = [title.get("title")]
            writer.writerow(a + b)
