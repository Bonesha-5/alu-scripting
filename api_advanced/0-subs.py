#!/usr/bin/python3
"""Module that queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    sub = response.json().get("data", {}).get("subscribers", 0)
    return sub
