#!/usr/bin/python3
"""
This script counts the number of occurrences of a list of words in the titles of the top
100 hot posts on a given subreddit using the Reddit API.
"""
import requests


def count_words(subreddit, word_list):
    """
    This function counts the number of occurrences of the given list of words in the titles of
    the top 100 hot posts of the specified subreddit and prints the counts in descending order.

    :param subreddit: The subreddit to search.
    :param word_list: The list of words to search for in the titles of the subreddit's posts.
    :return: None
    """
    # Initialize a dictionary to hold the count of occurrences of each word
    word_dict = {}

    # Base URL for the Reddit API
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set headers to identify the script as a user agent
    headers = {"User-Agent": "Mozilla/5.0"}

    # Set parameters for the API request
    params = {"limit": 100}

    # Make the initial request to the Reddit API
    response = requests.get(base_url, headers=headers, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response as JSON
        response_data = response.json()

        # Iterate over the posts in the response
        for post in response_data["data"]["children"]:
            # Get the title of the post
            title = post["data"]["title"]

            # Iterate over the words in the word list
            for word in word_list:
                # Check if the word appears in the title
                if word in title.lower():
                    # If the word is not in the word dictionary, add it with a count of 1
                    if word not in word_dict:
                        word_dict[word] = 1
                    # If the word is in the dictionary, increment its count by 1
                    else:
                        word_dict[word] += 1

        # Sort the dictionary by the count of occurrences of each word (in descending order)
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        # Print the results
        for word, count in sorted_words:
            print("{}: {}".format(word, count))

    else:
        # If the response was not successful, print an error message
        print("An error occurred while fetching data from the Reddit API. Please try again later.")
