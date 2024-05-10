'''
this python file is from a web scraping tutorial where it recommends
movies after it grabs a list from the internet
It will be used as a baseline for the Docker bit

'''

import random
import requests # pip install requests
from bs4 import BeautifulSoup #pip install bs4

url = 'https://www.imdb.com/chart/top'

# 