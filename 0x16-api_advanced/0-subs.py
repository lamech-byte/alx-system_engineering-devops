#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
    subreddit: The subreddit name as a string.

    Returns:
    The number of subscribers as an integer.
    If an invalid subreddit is given, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "My User Agent"
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        data = response.json().get("data")
        return data.get("subscribers")
