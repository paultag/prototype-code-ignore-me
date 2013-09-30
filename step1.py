import requests
import os

OPENSTATES_BASE = "http://openstates.org/api/v1"
API_KEY = open(
    os.path.abspath(os.path.expanduser("~/.sunlight.key")), 'r').read().strip()


def create_url(method):
    return OPENSTATES_BASE + "/" + method


def request_data(method):
    url = create_url(method)
    params = {"apikey": API_KEY,}
    return requests.get(url, params=params).json()


def metadata():
    return request_data('metadata')


for b in metadata():
    print b['name']
