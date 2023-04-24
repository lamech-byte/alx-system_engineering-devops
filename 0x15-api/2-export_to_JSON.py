#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    user_id = sys.argv[1]
    # URL of the API endpoint to get the employee information
    url = "https://jsonplaceholder.typicode.com/"
    # Get the employee information
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    # Get the employee's tasks
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
