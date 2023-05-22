#!/usr/bin/python3
""" Script that uses REST API to export data in
the CSV format."""
import requests
import sys
import csv


if __name__ == '__main__':
    employee_id = sys.argv[1]

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)

    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(
             employee_id)

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()

        response = requests.get(employee_url)
        response.raise_for_status()
        employee = response.json()

        user_id = str(employee['id'])
        filename = "{}.csv".format(user_id)

        rows = []

        for todo in todos:
            task_completed_status = str(todo['completed'])
            task_title = todo['title']
            rows.append([
                user_id,
                employee['username'],
                task_completed_status,
                task_title
                ])

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("CSV file '{}' has been exported sucessfully.".format(
            filename))

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
