#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee data and todo list from REST API."""
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    # Get employee details
    response = requests.get(employee_url)
    employee = response.json()
    employee_name = employee.get('name')

    # Get employee's todos
    todos_url = f"{employee_url}/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    return employee_name, tasks


def process_tasks(tasks):
    """Process list of tasks to count completed ones and gather their titles"""
    done_tasks = [task for task in tasks if task.get('completed')]
    done_count = len(done_tasks)
    return done_count, done_tasks


def print_employee_tasks(employee_name, done_count, total_tasks, done_tasks):
    """Print employee's task completion summary, titles of completed tasks"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_count, total_tasks))
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    employee_id = sys.argv[1]
    employee_name, tasks = fetch_employee_data(employee_id)
    done_count, done_tasks = process_tasks(tasks)
    print_employee_tasks(employee_name, done_count, len(tasks), done_tasks)
