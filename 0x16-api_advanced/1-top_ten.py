#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Mycustomer/1.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)

    try:
        response = requests.get(url, headers=user, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title', None))
    except Exception:
        print(e)
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
