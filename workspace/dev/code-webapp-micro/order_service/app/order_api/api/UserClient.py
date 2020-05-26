from flask import session
import requests
import dns.resolver

def dns_resolve(domain):
        srvInfo = {}
        srv_records=dns.resolver.query('_user._tcp.'+domain, 'SRV')
        for srv in srv_records:
            srvInfo['weight']   = srv.weight
            srvInfo['host']     = str(srv.target).rstrip('.')
            srvInfo['priority'] = srv.priority
            srvInfo['port']     = srv.port
        return 'http://'+srvInfo['host']+':'+str(srvInfo['port'])


class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        response = requests.request(method="GET", url=dns_resolve('servicediscovery.internal')+'/api/user', headers=headers)
        if response.status_code == 401:
            return False

        user = response.json()
        return user
