import pocket
import json
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import os

POCKET_APP_KEY = os.environ['POCKET_APP_KEY']


def pocket_get(accessToken, detailType, count, offset, since):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    return instance.get(state='all', detailType=detailType, count=count, offset=offset, since=since, sort='oldest')[0]['list']


def pocket_archive(accessToken, itemId):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    instance.archive(itemId)
