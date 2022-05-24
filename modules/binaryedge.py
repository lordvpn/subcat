import navigator
import os

BINARYEDGE_API_KEY = os.getenv('BINARYEDGE_API_KEY')
URL_API = 'https://api.binaryedge.io/v2/query/domains/subdomain/{0}'
DOMAINS_LIST = []


def returnDomains(domain, silent=False):
    req = navigator.Navigator()
    json = req.downloadResponse(URL_API.format(domain), 'JSON', 'GET', header={'X-Key': BINARYEDGE_API_KEY})
    try:
        for _ in json['events']:
            DOMAINS_LIST.append(_)
        if not silent:
            req.ModuleLoaded('binaryedge.io', DOMAINS_LIST)
        return DOMAINS_LIST
    except:
        return []
