#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open(f"{employee_id}.csv", 'w') as file:
        file.write('"Employee ID","Username","Completed","Title"\n')
        for task in tasks:
            file.write('"{}", "{}", {}, "{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))
