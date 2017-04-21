import pocket
import json
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import os

POCKET_APP_KEY = os.environ['POCKET_APP_KEY']


def fetch_pocket_links(accessToken, detailType, count, offset, since):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    return instance.get(state='all', detailType=detailType, count=count, offset=offset, since=since, sort='oldest')[0]['list']


def save_pocket_links():
    article_list = fetch_pocket_links()
    json_article_list = json.dumps(article_list)
    file_article_list = open('articles.json', 'w+')
    file_article_list.write(json_article_list)
    file_article_list.close()
