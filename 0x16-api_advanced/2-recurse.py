#!/usr/bin/python3

"""
Using Reddit's API to retrieve hot post titles.
"""

import requests

after = None


def recurse(subreddit, hot_list=[]):
    """Recursively returning the titles of hot posts."""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}

    response = requests.get(
            url, params=parameters, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
