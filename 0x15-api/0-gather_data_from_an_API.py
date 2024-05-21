#!/usr/bin/python3
"""Accessing a REST API for employee to-do lists"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    completed = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee %s is done with tasks(%d/%d):"
          % (employee_name, completed, len(tasks)))

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
