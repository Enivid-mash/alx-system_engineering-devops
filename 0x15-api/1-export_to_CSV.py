#!/usr/bin/python3
"""Accesses a REST API for todo lists of employees and writing to a CSV file"""

import requests
import sys
import csv


def fetch_employee_data(employee_id):
    """Fetch employee username and tasks from REST API."""
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    # Get employee details
    response = requests.get(employee_url)
    employee = response.json()
    username = employee.get('username')

    # Get employee's todos
    todos_url = f"{employee_url}/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    return username, tasks


def write_tasks_to_csv(employee_id, username, tasks):
    """Write tasks to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, username, task.get('completed'),
                            task.get('title')])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    username, tasks = fetch_employee_data(employee_id)
    write_tasks_to_csv(employee_id, username, tasks)
