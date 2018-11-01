#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from lxml import html
import re
import os

USERNAME = "yun+1@salmonellaville.com"
PASSWORD = "iloveyammer"
Base_URL = "https://www.staging.yammer.com/login?locale=en-US&locale_type=standard"
Login_URL = 'https://www.staging.yammer.com/session'
session_requests = requests.session()

def get_token():
    # Get login token
    index_page = session_requests.get(Base_URL)
    tree = html.fromstring(index_page.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
    return authenticity_token

def gihub_login(authenticity_token):
    # Create payload
    data= {
        "utf8":"✓",
        "network_permalink": '',
        "authenticity_token":authenticity_token,
        "login":USERNAME,
        "password":PASSWORD,
        "remember_me=":"on"
    }
    # Perform login
    response = session_requests.post(Login_URL,data=data)
    print(response.status_code)

def download_image(url):
    image = session_requests.get(url)
    if image.status_code == 200:
        open('logo.jpg', 'wb').write(image.content)

def main():
    authenticity_token = get_token()
    gihub_login(authenticity_token)
    download_image("https://www.staging.yammer.com/api/v1/uploaded_files/10774758/download")

if __name__ == '__main__':
    main()