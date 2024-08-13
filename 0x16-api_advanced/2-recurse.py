#!/usr/bin/python3
"""Script to paginate response"""

import requests


def recurse(subreddit, hot_lst=[], page=1, limit=100):
    """A recursive function that queries the Reddit API
    returns a list containing the titles
    of all hot articles for a given subreddit.
    """

    if len(hot_lst) >= limit:
        return hot_lst

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"page": page}
    headers = {
        "User-Agent": "Mozilla"
    }

    res = requests.get(url, params=params, headers=headers)
    if res.status_code == 404:
        return None
    data = res.json()

    if "data" in data and "children" in data["data"]:
        articles = data["data"]["children"]
        for article in articles:
            hot_lst.append(article["data"]["title"])

    if "data" in data and "after" in data["data"]:
        page += 1
        return recurse(subreddit, hot_lst, page)
    return hot_lst