import requests
OPENSTATES_BASE = "http://openstates.org/api/v1"


def create_url(method, *args, **kwargs):
    return "{base}/{method}/{params}".format(
        base=OPENSTATES_BASE,
        method=method,
        params="/".join(args)
    )



def request_data(method, *args, **kwargs):
    url = create_url(method, *args, **kwargs)
    params = kwargs.copy()
    params.update({"apikey": "APIKEY",})
    print url, params
    return requests.get(url, params=params).json()


def metadata(place):
    return request_data('metadata', place)


def bills(**search):
    return request_data('bills', **search)


def bill(state, session, bill_id):
    return request_data('bills', state, session, bill_id)


def lookup_legislators(lat, lon):
    return request_data(
        'legislators',
        'geo',
        lat=lat,
        long=lon
    )


for person in lookup_legislators(40.00, -100):
    print person['full_name']


#for b in bills(state='oh', q='beer'):
#    info = bill(b['state'], b['session'], b['bill_id'])
#    print info['title']
