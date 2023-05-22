#!/usr/bin/python3
""" Script that uses REST API to export data in
the CSV format."""
import requests
import json


if __name__ == '__main__':
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(todos_url)
        response.raise_for_status()
        todos = response.json()

        response = requests.get(users_url)
        response.raise_for_status()
        users = response.json()

        filename = "todo_all_employees.json"

        json_data = {}

        for user in users:
            user_id = str(user['id'])
            username = user['username']
            json_data[user_id] = []

            for todo in todos:
                if todo['userId'] == user['id']:
                    task_completed_status = todo['completed']
                    task_title = todo['title']
                    json_data[user_id].append({
                        "username": username,
                        "task": task_title,
                        "completed": task_completed_status
                        })

        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)

        print("JSON file '{}' has been exported sucessfully.".format(
            filename))

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
