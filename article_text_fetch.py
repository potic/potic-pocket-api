import json
from bs4 import BeautifulSoup
import urllib2
import re

article_file = open('articles.json', 'r')
article_map = json.loads(article_file.read())
article_texts = []
for l in article_map.keys():
    try:
        response = urllib2.urlopen(article_map[l]['resolved_url'])
        text = response.read()
        text = BeautifulSoup(text)
        to_extract = text.findAll('script')
        for item in to_extract:
            item.extract()
        to_extract = text.findAll('style')
        for item in to_extract:
            item.extract()

        text = text.get_text()
        text = re.sub('(\n)+', '\n', text)

        re.sub("\n(\n)*", "\n", text)
        f = open('articles/' + l + '.txt', 'w+')
        f.write(text.encode('utf-8'))
        # f.write(text)
        f.close()
        print 'finished with one'
    except Exception:
        print 'oooooops'

article_file.close()
