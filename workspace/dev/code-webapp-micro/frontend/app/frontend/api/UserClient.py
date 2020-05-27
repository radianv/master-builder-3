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
    def post_login(form):
        api_key = False
        payload = {
            'username': form.username.data,
            'password': form.password.data,
        }
        url = dns_resolve('servicediscoveryVA.internal')+'/api/user/login'
        #url = 'http://ecs-s-ECSAL-1LSW6XFAGQQS3-818649976.ca-central-1.elb.amazonaws.com/api/user/login'
        response = requests.request("POST", url=url, data=payload)
        if response:
            d = response.json()
            if d['api_key'] is not None:
                api_key = d['api_key']
        return api_key

    @staticmethod
    def does_exist(username):
        url = dns_resolve('servicediscoveryVA.internal')+'/api/user/'+username+'/exist'
        #url = 'http://ecs-s-ECSAL-1LSW6XFAGQQS3-818649976.ca-central-1.elb.amazonaws.com/api/user/'+username+'/exist'
        response = requests.request("GET", url=url)
        return response.status_code == 200

    @staticmethod
    def post_user_create(form):
        user = False
        payload = {
            'email': form.email.data,
            'password': form.password.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'username': form.username.data
        }
        url = dns_resolve('servicediscoveryVA.internal')+'/api/user/create'
        #url = 'http://ecs-s-ECSAL-1LSW6XFAGQQS3-818649976.ca-central-1.elb.amazonaws.com/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def get_user():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }

        response = requests.request(method="GET", url=dns_resolve('servicediscoveryVA.internal')+'/api/user', headers=headers)
        #response = requests.request(method="GET", url='http://ecs-s-ECSAL-1LSW6XFAGQQS3-818649976.ca-central-1.elb.amazonaws.com/api/user', headers=headers)
        user = response.json()
        return user
