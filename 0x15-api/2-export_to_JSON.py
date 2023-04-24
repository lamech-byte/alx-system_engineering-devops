#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line arguments
    user_id = sys.argv[1]
    
    # URL of the API endpoint to get the employee information
    url = "https://jsonplaceholder.typicode.com/"
    
    # Get the employee information
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    
    # Get the employee's tasks
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    
    # Export the tasks in JSON format
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
