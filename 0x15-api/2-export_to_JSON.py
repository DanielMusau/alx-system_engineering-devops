#!/usr/bin/python3
""" Script that uses REST API to export data in
the CSV format."""
import requests
import sys
import json


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
        filename = "{}.json".format(user_id)

        json_data = {
                user_id: []
                }

        for todo in todos:
            task_completed_status = todo['completed']
            task_title = todo['title']
            username = employee['username']
            json_data[user_id].append({
                "task": task_title,
                "completed": task_completed_status,
                "username": username
                })

        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)

        print("JSON file '{}' has been exported sucessfully.".format(
            filename))

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
