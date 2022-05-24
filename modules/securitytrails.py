import navigator
import os

SECURITYTRAILS_API_KEY = os.getenv('SECURITYTRAILS_API_KEY')
URL_API = 'https://api.securitytrails.com/v1/domain/{0}/subdomains'
DOMAINS_LIST = []


def returnDomains(domain, silent=False):
    req = navigator.Navigator()
    json = req.downloadResponse(URL_API.format(domain), 'JSON', 'GET', header={'apikey': SECURITYTRAILS_API_KEY})
    try:
        for _ in json['subdomains']:
            DOMAINS_LIST.append('{0}.{1}'.format(_, domain))
        if not silent:
            req.ModuleLoaded('securitytrails.com', DOMAINS_LIST)
        return DOMAINS_LIST
    except:
        return []
