#!/usr/bin/python3
"""Module for querying the Reddit API to get subreddit subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'keviScript/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if data:
        return data.get("subscribers", 0)
    return 0
