import requests
import os

OPENSTATES_BASE = "http://openstates.org/api/v1"
API_KEY = open(
    os.path.abspath(os.path.expanduser("~/.sunlight.key")), 'r').read().strip()


def create_url(method, *args):
    return OPENSTATES_BASE + "/" + method + "/" + "/".join(args)


def request_data(method, *args):
    url = create_url(method, *args)
    params = {"apikey": API_KEY,}
    return requests.get(url, params=params).json()


def metadata(state=None):
    if state:
        return request_data('metadata', state)
    else:
        return request_data('metadata')


ohio = metadata("oh")
print ohio['name']
