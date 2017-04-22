from flask import Flask, request
import requests
import json
from article_fetch import fetch_pocket_links

app = Flask(__name__)


@app.route('/fetch_cached')
def fetch_cached():
    return open('articles.json', 'r').read()


@app.route('/fetch/<user_id>')
def fetch(user_id):
    detailType = request.args.get('detailType')
    if not detailType:
        detailType = 'complete'

    count = request.args.get('count')
    if not count:
        count = 10
    else:
        count = int(count)

    offset = request.args.get('offset')
    if not offset:
        offset = 0
    else:
        offset = int(offset)

    since = request.args.get('since')
    if not since:
        since = 0
    else:
        since = int(since)

    userResponse = requests.get('http://pocket-square-users:8080/user/' + user_id).json()
    return json.dumps(fetch_pocket_links(userResponse["accessToken"], detailType, count, offset, since))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
