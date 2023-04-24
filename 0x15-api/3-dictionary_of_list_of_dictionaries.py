#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    # retrieve all users
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    # create a dictionary to group tasks by user ID and export to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
