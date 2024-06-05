#!/usr/bin/python3

"""
Retrieve the number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(api_url, headers=headers)
    data = response.json()

    try:
        return data.get('data').get('subscribers')

    except Exception:
        return 0
