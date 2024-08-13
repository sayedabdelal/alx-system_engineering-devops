#!/usr/bin/python3
""" a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0