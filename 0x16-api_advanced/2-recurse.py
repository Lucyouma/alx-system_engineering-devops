#!/usr/bin/python3
"""
module to recurseively query
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively querry a subreddit and return hit posts
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)

    if not hot_list:
        hot_list = []

    try:
        response = requests.get(url, params=params, headers=headers,
                                allow_redirects=False)
        response_data = response.json()['data']['children']

        if not response_data:
            return hot_list

        hot_list.extend(item['data']['title'] for item in response_data)

        after = response_data[-1]['data']['name']

        if not after:
            return hot_list

        return (hot_list + recurse(subreddit, hot_list=hot_list, after=after))
    except Exception as e:
        return None
