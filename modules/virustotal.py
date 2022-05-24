import navigator
import os

VT_API_KEY = os.getenv('VT_API_KEY')
URL_API = 'https://www.virustotal.com/vtapi/v2/domain/report?domain={0}&apikey={1}'
DOMAINS_LIST = []


def returnDomains(domain, silent=False):
    req = navigator.Navigator()
    json = req.downloadResponse(URL_API.format(domain, VT_API_KEY), 'JSON', 'GET')
    try:
        for _ in json['subdomains']:
            if domain in _ and '*' not in _:
                DOMAINS_LIST.append(_)
        if not silent:
            req.ModuleLoaded('virustotal', DOMAINS_LIST)
        return DOMAINS_LIST
    except:
        return []
