from flask import Flask
from article_fetch import fetch_pocket_links
import json

app = Flask(__name__)


@app.route('/fetch_cached')
def fetch_cached():
    return open('articles.json', 'r').read()


@app.route('/fetch')
def fetch():
    return json.dumps(fetch_pocket_links())


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)