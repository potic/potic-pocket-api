import pocket
import json
import urllib2
from bs4 import BeautifulSoup
import sqlite3

POCKET_APP_KEY = '51208-f9d6fc146c43b2912ff314fa'
#POCKET_REQUEST_TOKEN = 'f43f5796-d630-3803-f038-1e8077'
POCKET_ACCESS_TOKEN = 'f3d74179-cda8-2a61-5011-847754'


def fetch_pocket_links():
    instance = pocket.Pocket(POCKET_APP_KEY, POCKET_ACCESS_TOKEN)
    return instance.get(state='all', detailType='complete', count=1000, sort='oldest')[0]['list']


def save_pocket_links():
    article_list = fetch_pocket_links()
    json_article_list = json.dumps(article_list)
    file_article_list = open('articles.json', 'w+')
    file_article_list.write(json_article_list)
    file_article_list.close()
