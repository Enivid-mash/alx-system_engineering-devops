#!/usr/bin/python3

"""
Prints the title of the first 10 posts.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    if not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = requests.get(url, headers=user_agent, params=params)
    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title', "None"))
    except (ValueError, KeyError):
        print("None")
