from flask import session
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


class OrderClient:

    @staticmethod
    def get_order():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = dns_resolve('servicediscovery.internal')+'/api/order'
        response = requests.request(method="GET", url = url, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def update_order(items):

        url = dns_resolve('servicediscovery.internal')+'/api/order/update'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=items, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_add_to_cart(product_id, qty=1):
        payload = {
            'product_id': product_id,
            'qty': qty,
        }
        url = dns_resolve('servicediscovery.internal')+'/api/order/add-item'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=payload, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_checkout():
        url = dns_resolve('servicediscovery.internal')+'/api/order/checkout'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data={}, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def get_order_from_session():
        default_order = {
            'items': {},
            'total': 0,
        }
        return session.get('order', default_order)


