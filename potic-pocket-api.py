from flask import Flask, request
import requests
import json
from pocket_api import pocket_get
from pocket_api import pocket_archive

app = Flask(__name__)


@app.route('/get/<user_id>')
def get(user_id):
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

    userResponse = requests.get('http://188.166.174.189:28101/user/' + user_id).json()
    return json.dumps(pocket_get(userResponse["accessToken"], detailType, count, offset, since))


@app.route('/archive/<user_id>/<item_id>')
def archive(user_id, item_id):
    userResponse = requests.get('http://188.166.174.189:28101/user/' + user_id).json()
    pocket_archive(userResponse["accessToken"], item_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
