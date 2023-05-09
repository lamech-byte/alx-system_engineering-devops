#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


sesion = requests.Session()
sesion.headers.update({'User-agent': 'My User Agent'})
sesion.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    URL = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    req = sesion.get(URL).json()
    try:
        for i in req['data']['children']:
            hot_list.append(i['data']['title'])
        if req['data']['after']:
            sesion.params = {'after': req['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None
