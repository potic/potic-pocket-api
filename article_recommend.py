import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import urllib2

article_file = open('articles.json', 'r')
article_map = json.loads(article_file.read())
article_texts = []
article_titles = []
for l in article_map.keys():
    try:
        f = open('articles/' + l + '.txt', 'r')
        article_texts.append(f.read())
        article_titles.append(article_map[l]['resolved_title'])
        f.close()
    except Exception:
        print 'something went wrong'

article_file.close()

tfidf = TfidfVectorizer().fit_transform(article_texts)
print type(tfidf)
# pairwise_similarity = tfidf * tfidf.T
cosine_similarities = linear_kernel(tfidf[62:63], tfidf).flatten()
# print pairwise_similarity.A
related_docs_indices = cosine_similarities.argsort()[-10:]
print related_docs_indices

for ind in reversed(related_docs_indices):
    print article_titles[ind]
