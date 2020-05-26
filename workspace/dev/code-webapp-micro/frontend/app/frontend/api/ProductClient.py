import requests
import dns.resolver

def dns_resolve(domain):
        srvInfo = {}
        srv_records=dns.resolver.query('_order._tcp.'+domain, 'SRV')
        for srv in srv_records:
            srvInfo['weight']   = srv.weight
            srvInfo['host']     = str(srv.target).rstrip('.')
            srvInfo['priority'] = srv.priority
            srvInfo['port']     = srv.port
        return 'http://'+srvInfo['host']+':'+str(srvInfo['port'])

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url = dns_resolve('servicediscovery.internal')+'/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(url = dns_resolve('servicediscovery.internal')+'/api/products')
        products = r.json()
        return products
