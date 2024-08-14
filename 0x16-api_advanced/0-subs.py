#!/usr/bin/python3
"""
0x16. API advanced
"""
import requests


def number_of_subscribers(subreddit):
    """A function that returns the number of subscribers
    to an account if existed."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
        url,
        headers={"User-Agent": "custom"},
    )
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
