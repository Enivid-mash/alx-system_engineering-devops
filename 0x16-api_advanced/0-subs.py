#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given subreddit.
"""

import requests


def get_subscriber_count(subreddit):
    """
    Fetches the subscriber count from Reddit's API for a specific subreddit.

    Args:
        subreddit: The name of the subreddit (e.g., "learnpython").

    Returns:
        The number of subscribers for the subreddit, or 0 if an error occurs.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    # Set a custom user-agent header
    headers = {'User-Agent': 'MyCoolScript/1.0'}

    # Build the API endpoint URL with string formatting
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data.get('data', {}).get('subscribers', 0)

    except requests.exceptions.RequestException:
        return 0
