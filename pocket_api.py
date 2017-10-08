import pocket
import os
import os.path

if 'POCKET_APP_KEY' in os.environ:
    POCKET_APP_KEY = os.environ['POCKET_APP_KEY']
if os.path.isfile('pocket-app.key'):
    with open('pocket-app.key', 'r') as pocketAppKeyFile:
        POCKET_APP_KEY = pocketAppKeyFile.read().replace('\n', '')


def pocket_get(accessToken, detailType, count, offset, since):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    return instance.get(state='all', detailType=detailType, count=count, offset=offset, since=since, sort='oldest')[0]['list']


def pocket_archive(accessToken, itemId):
    instance = pocket.Pocket(POCKET_APP_KEY, accessToken)
    return instance.archive(itemId, wait=False)
