#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''
api_headers = {
    'Accept': 'application/json',
    'User-Agent': ' '.join([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'AppleWebKit/537.36 (KHTML, like Gecko)',
        'Chrome/97.0.4692.71',
        'Safari/537.36',
        'Edg/97.0.1072.62'
    ])
}


def number_of_subscribers(subreddit):

    """returns the number of subscribers for a given subreddit"""
    
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get(
        '{}/r/{}/about.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if r.status_code == 200:
        return r.json()['data']['subscribers']
    return 0
