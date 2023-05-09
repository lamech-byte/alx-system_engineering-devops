#!/usr/bin/python3
"""
This script counts the number of occurrences of a list of words in the titles of the top
100 hot posts on a given subreddit using the Reddit API.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    This function counts the number of occurrences of the given list of words in the titles of
    the top 100 hot posts of the specified subreddit and prints the counts in descending order.

    :param subreddit: The subreddit to search.
    :param word_list: The list of words to search for in the titles of the subreddit's posts.
    :return: None
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
