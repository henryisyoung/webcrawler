#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from lxml import html
import re

USERNAME = "yun+1@salmonellaville.com"
PASSWORD = "iloveyammer"
Base_URL = "https://www.staging.yammer.com" #"https://github.com/login"
Login_URL = 'https://www.staging.yammer.com/session' #"https://github.com/session"

def get_github_html(url):
    '''
    这里用于获取登录页的html，以及cookie
    :param url: https://github.com/login
    :return: 登录页面的HTML,以及第一次的cooke
    '''
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return first_cookie


def main():
    session_requests = requests.session()

    # Get login csrf token
    agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    headers = {
        "Host": "www.staging.yammer.com",
        "Referer": "https://www.staging.yammer.com",
        'User-Agent': agent
    }

    index_url = 'https://www.staging.yammer.com/login?'
    index_page = session_requests.get(index_url, headers=headers)
    tree = html.fromstring(index_page.text)

    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    # Create payload
    data= {
        # "commit": "Sign in",
        "utf8":"✓",
        "network_permalink": '',
        "authenticity_token":authenticity_token,
        "login":"zyun3939@gmail.com",
        "password":"evring89668",
        "remember_me=":"on"
    }

    # Perform login
    cookie = get_github_html(Base_URL)
    response = requests.post(Login_URL,data=data,cookies=cookie)

    print(response.status_code)
    cookie = response.cookies.get_dict()
    
    # Scrape url
    response = requests.get("https://www.staging.yammer.com/salmonellaville.com/users?letter=A",cookies=cookie)
    print(response.text)


if __name__ == '__main__':
    main()