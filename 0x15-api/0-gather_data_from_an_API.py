#!/usr/bin/python3
""" Script that uses REST API for a given
employee ID, returns information about his/
her TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)

    try:
        response = requests.get(url)
        response.raise_for_status()
        todos = response.json()

        completed_tasks = [todo for todo in todos if todo['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_tasks = len(todos)

        employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(
                employee_id)
        response = requests.get(employee_url)
        response.raise_for_status()
        employee = response.json()
        employee_name = employee['name']

        print("Employee {} is done with tasks ({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
