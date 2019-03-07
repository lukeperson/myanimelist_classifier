# Author: Luke Tan
# Date: 07/03/19
#
# Scraper.py - Download ten character images given anime link 

import requests
from bs4 import BeautifulSoup
import re
import urllib.request


# Assertion: Returns "SUCC" when file successfully downloaded "FAIL" otherwise
# Searches through all a links and performs a regex pattern search to find name
# of jpg
def downloadImage(num, name):
    pat = r'https(.+?)jpg'

    page = requests.get('https://myanimelist.net/character/' + num)
    soup = BeautifulSoup(page.text, 'html.parser')

    for a in soup.find_all('a', href=True):
        if '/character/' + num in str(a):
            m = re.search(pat, str(a))
            if m:
                url = m.group(0)
                urllib.request.urlretrieve(url, name + '.jpg')
                return "SUCC"
    return "FAIL"

# Searches through all a links on anime page and adds any characters to
# char_array
# 
def scrapeAnime(page):
    page = requests.get(page)

    soup = BeautifulSoup(page.text, 'html.parser')

    char_array = []

    for a in soup.find_all('a', href=True):
        if 'https://myanimelist.net/character/' in str(a):
            char_array.append(a['href'])

    index = 0
    while index < 10:
        # There are two a links for each character so pop one use the other
        char_array.pop(index)
        linkArray = char_array[index].split('/')
        print(downloadImage(linkArray[4], linkArray[5]) + ":" + char_array[index])
        index += 1


