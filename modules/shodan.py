from datetime import datetime

import navigator
import os

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')
URL_API = 'https://api.shodan.io/dns/domain/{0}?key={1}'
DOMAINS_LIST = []


def returnDomains(domain, silent=False):
    req = navigator.Navigator()
    json = req.downloadResponse(URL_API.format(domain, SHODAN_API_KEY), 'JSON', 'GET')
    try:
        for _ in json['subdomains']:
            DOMAINS_LIST.append('{0}.{1}'.format(_, domain))
        if not silent:
            req.ModuleLoaded('shodan.io', DOMAINS_LIST)
        return DOMAINS_LIST
    except:
        return []
