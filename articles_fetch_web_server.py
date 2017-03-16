from flask import Flask
import requests
import json
from article_fetch import fetch_pocket_links

app = Flask(__name__)


@app.route('/fetch_cached')
def fetch_cached():
    return open('articles.json', 'r').read()


@app.route('/fetch/<user_id>')
def fetch(user_id):
    count = request.args.get('count')
    offset = request.args.get('offset')

    request = requests.get('http://pocket-square-users:8080/user/' + user_id)
    response = request.json()
    return json.dumps(fetch_pocket_links(response["accessToken"], count, offset))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
