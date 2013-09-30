import requests
import os

OPENSTATES_BASE = "http://openstates.org/api/v1"
API_KEY = open(
    os.path.abspath(os.path.expanduser("~/.sunlight.key")), 'r').read().strip()


def create_url(method, *args):
    return OPENSTATES_BASE + "/" + method + "/" + "/".join(args)


def request_data(method, *args, **kwargs):
    url = create_url(method, *args)
    params = kwargs.copy()
    params.update({"apikey": API_KEY,})
    return requests.get(url, params=params).json()


def legislators(lat, long):
    return request_data('legislators', 'geo',
                        lat=lat,
                        long=long)


for leg in legislators(44, -70):
    print leg['full_name']
