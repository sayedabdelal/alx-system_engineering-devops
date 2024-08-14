#!/usr/bin/python3
"""The possibilty to found sudit."""
import requests


def top_ten(subreddit):
    """Print the from a particular subreddit."""
    leen = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(leen, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
