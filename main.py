import json
import urllib.request


def get_from_json(file_name: str = None) -> json.load:
    file_name = './addNote.json'
    # file_name = './guiAddCards.json'
    # Retrieve JSON data from the file
    with open(file_name, "r") as file:
        data = json.load(file)
    return data


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    # requestJson = json.dumps(request(action, **params)).encode('utf-8')
    # response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))

    requestJson = json.dumps(get_from_json()).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))

    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


result = invoke('deckNames')
print('got list of decks: {}'.format(result))
