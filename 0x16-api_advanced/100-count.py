#!/usr/bin/python3

"""Reddit API"""

import json
import requests


def count_words(subreddit, word_list, next_page_token="", word_count=[]):
    """Count occurrences of specified words in subreddit titles."""

    if not next_page_token:
        word_count = [0] * len(word_list)

    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(api_url,
                             params={'after': next_page_token},
                             allow_redirects=False,
                             headers={'User-Agent': 'bhalut'})

    if response.status_code == 200:
        response_data = response.json()

        for post in response_data['data']['children']:
            for word in post['data']['title'].split():
                for idx, target_word in enumerate(word_list):
                    if target_word.lower() == word.lower():
                        word_count[idx] += 1

        next_page_token = response_data['data']['after']
        if next_page_token is None:
            duplicates = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        duplicates.append(j)
                        word_count[i] += word_count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (word_count[j] > word_count[i] or
                        (word_list[i] > word_list[j] and word_count[j] == word_count[i])):
                        word_count[i], word_count[j] = word_count[j], word_count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            for i in range(len(word_list)):
                if word_count[i] > 0 and i not in duplicates:
                    print("{}: {}".format(word_list[i].lower(), word_count[i]))
        else:
            count_words(subreddit, word_list, next_page_token, word_count)
