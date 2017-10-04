from flask import Flask, request
import json
from pocket_api import pocket_get
from pocket_api import pocket_archive

app = Flask(__name__)


@app.route('/get/<access_token>')
def get(access_token):
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

    return json.dumps(pocket_get(access_token, detailType, count, offset, since))


@app.route('/archive/<access_token>/<item_id>', methods=['POST'])
def archive(access_token, item_id):
    pocket_archive(access_token, item_id)
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
