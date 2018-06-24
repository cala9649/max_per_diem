#!/usr/bin/python3
#
# Thanks to Michael J for his Wikipedia County Table
# Found at https://en.wikipedia.org/wiki/User:Michael_J/County_table

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = urlopen("https://en.wikipedia.org/wiki/User:Michael_J/County_table")
page_soup = BeautifulSoup(page, 'html.parser')
counties_table = page_soup.find('table', attrs={'class': 'wikitable'})
with open("counties_info.txt", "w") as f:
    for row in counties_table.findAll('tr'):
        cells = row.findAll('td')
        if cells:
            state = cells[1].text
            name = cells[3].text
            lat = cells[12].text.replace("+", "").replace("°", "")
            lon = cells[13].text.replace("–", "-").replace("°", "")
            f.write(state + " " + name + " " + lat + " " + lon + "\n")
