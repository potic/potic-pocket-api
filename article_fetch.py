import pocket
import json
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import os

POCKET_APP_KEY = os.environ['POCKET_SQUARE_APP_KEY']


def fetch_pocket_links(accessToken):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    return instance.get(state='all', detailType='complete', count=1000, sort='oldest')[0]['list']


def save_pocket_links():
    article_list = fetch_pocket_links()
    json_article_list = json.dumps(article_list)
    file_article_list = open('articles.json', 'w+')
    file_article_list.write(json_article_list)
    file_article_list.close()
