#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
import time

def count_words(subreddit, word_list, last_post_id=None, word_dict=None):
    if word_dict is None:
        word_dict = {}
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={last_post_id}"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {}).get("children", [])
    if not data:
        return None
    if last_post_id is None:
        word_dict = {}
    for post in data:
        title_words = post["data"]["title"].split()
        for word in title_words:
            word = word.lower().strip(".,!?:;-_")
            if word in word_list:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    if last_post_id is None and len(word_dict) == 0:
        return None
    if last_post_id is None:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1],
